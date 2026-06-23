"""
将 siteinfoApp/data.py 中的默认展示数据同步到数据库。
运行方式: python manage.py sync_default_data
"""
import os
import shutil

from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date

from contentApp.models import Achievement, Article, RobotProject
from siteinfoApp import data
from siteinfoApp.models import Carousel, Member


CATEGORY_MAP = {
    '招新信息': 'recruit',
    '赛事动态': 'competition',
    '技术文章': 'tech',
    '战队公告': 'notice',
    '训练记录': 'training',
    '合作交流': 'cooperation',
    '成果展示': 'achievement',
}

CAROUSEL_ITEMS = [
    {'page': 'home',  'filename': '1.jpg',              'title': 'LionHeart 机器人战队',  'subtitle': '让热爱成为战斗力', 'order': 0},
    {'page': 'home',  'filename': '41e172e986e8667a731edd47a00b3481.jpg', 'title': 'RoboMaster 机甲大师', 'subtitle': '强工程实践，强团队协作', 'order': 1},
    {'page': 'home',  'filename': '45154848b13081124ce923d8094a57f5.png', 'title': '战队研发训练',        'subtitle': '从实验室到赛场', 'order': 2},
    {'page': 'home',  'filename': '73be840f84823a8c4e88e163f50afb7b.jpeg', 'title': '机器人创新实践',      'subtitle': '机械 · 电控 · 视觉 · 导航', 'order': 3},
    {'page': 'home',  'filename': '767c09cdc56522648ffb87793d23a9de_720.jpg', 'title': '加入 LionHeart', 'subtitle': '以工程点燃热爱，以技术守护荣耀', 'order': 4},
    # 关于战队页面轮播图
    {'page': 'about', 'filename': '1.jpg',              'title': 'LionHeart 机器人战队',  'subtitle': '重庆三峡科技大学 · 以工程点燃热爱', 'order': 0},
    {'page': 'about', 'filename': '41e172e986e8667a731edd47a00b3481.jpg', 'title': '团队协作与工程实践',  'subtitle': '从课堂到赛场，从理论到实战', 'order': 1},
    {'page': 'about', 'filename': '73be840f84823a8c4e88e163f50afb7b.jpeg', 'title': '实验室日常',          'subtitle': '机械 · 电控 · 视觉 · 导航多方向协同', 'order': 2},
]

DEFAULT_MEMBERS = [
    {
        'name': '包俊',
        'gender': '男',
        'college': '智能制造学院',
        'major': '信息管理与信息系统',
        'group_name': '项目管理组',
        'position': '战队负责人',
        'description': '战队管理、项目统筹、机器人技术学习、赛事组织、招商合作。',
        'sort_order': 0,
    },
]


class Command(BaseCommand):
    help = '将 data.py 中的默认数据同步到数据库（已存在的会跳过）'

    def handle(self, *args, **options):
        self.sync_carousels()
        self.sync_members()
        self.sync_robots()
        self.sync_achievements()
        self.sync_news()
        self.stdout.write(self.style.SUCCESS('默认数据同步完成，请进入后台管理进行修改。'))

    def sync_carousels(self):
        src_dir = os.path.join(settings.BASE_DIR, 'static', '轮播图')
        dst_dir = os.path.join(settings.MEDIA_ROOT, 'carousel')
        os.makedirs(dst_dir, exist_ok=True)

        for item in CAROUSEL_ITEMS:
            if Carousel.objects.filter(title=item['title'], page=item['page']).exists():
                self.stdout.write(f'  - 轮播图已存在，跳过: [{item["page"]}] {item["title"]}')
                continue

            src_path = os.path.join(src_dir, item['filename'])
            dst_path = os.path.join(dst_dir, item['filename'])

            if not os.path.exists(src_path):
                self.stdout.write(self.style.WARNING(f'  ✗ 轮播图源文件不存在: {item["filename"]}'))
                continue

            shutil.copy2(src_path, dst_path)

            with open(dst_path, 'rb') as f:
                carousel = Carousel(
                    page=item.get('page', 'home'),
                    title=item['title'],
                    subtitle=item['subtitle'],
                    order=item['order'],
                    status=True,
                )
                carousel.image.save(item['filename'], File(f), save=True)

            self.stdout.write(f'  ✓ 轮播图: [{item["page"]}] {item["title"]}')

    def sync_members(self):
        for item in DEFAULT_MEMBERS:
            obj, created = Member.objects.get_or_create(
                name=item['name'],
                defaults={
                    'gender': item.get('gender', ''),
                    'college': item.get('college', ''),
                    'major': item.get('major', ''),
                    'group_name': item.get('group_name', ''),
                    'position': item.get('position', ''),
                    'description': item.get('description', ''),
                    'sort_order': item.get('sort_order', 0),
                    'status': True,
                },
            )
            if created:
                self.stdout.write(f'  ✓ 成员: {item["name"]}')
            else:
                self.stdout.write(f'  - 成员已存在，跳过: {item["name"]}')

    def sync_robots(self):
        for item in data.ROBOTS:
            obj, created = RobotProject.objects.get_or_create(
                name=item['name'],
                defaults={
                    'robot_type': item.get('type', ''),
                    'description': item.get('summary', ''),
                    'technical_features': '\n'.join(item.get('features', [])),
                    'hardware_config': item.get('hardware', ''),
                    'software_config': item.get('software', ''),
                    'progress': item.get('progress', ''),
                    'status': True,
                },
            )
            if created:
                self.stdout.write(f'  ✓ 机器人: {item["name"]}')
            else:
                # 更新已有的机器人数据
                obj.technical_features = '\n'.join(item.get('features', []))
                obj.hardware_config = item.get('hardware', '')
                obj.software_config = item.get('software', '')
                obj.save()
                self.stdout.write(f'  - 机器人已存在，已更新: {item["name"]}')

    def sync_achievements(self):
        for item in data.ACHIEVEMENTS:
            year_str = item.get('year', '')
            # 提取年份数字（处理 '2025 上半年' 这样的格式）
            import re
            year_match = re.match(r'(\d{4})', year_str)
            year = int(year_match.group(1)) if year_match else None
            try:
                award_date = date(year, 1, 1) if year else None
            except (ValueError, TypeError):
                award_date = None

            obj, created = Achievement.objects.get_or_create(
                competition_name=item.get('title', ''),
                defaults={
                    'description': item.get('detail', item.get('summary', '')),
                    'award_time': award_date,
                    'status': True,
                },
            )
            if created:
                self.stdout.write(f'  ✓ 成果: {item["title"]}')
            else:
                # 更新已有成果的描述
                obj.description = item.get('detail', item.get('summary', ''))
                obj.save()
                self.stdout.write(f'  - 成果已存在，已更新: {item["title"]}')

    def sync_news(self):
        for item in data.NEWS:
            category_key = CATEGORY_MAP.get(item.get('category', ''), 'notice')

            try:
                pub_date = timezone.datetime.strptime(
                    item.get('published_at', ''),
                    '%Y-%m-%d'
                ).replace(tzinfo=timezone.get_current_timezone())
            except (ValueError, TypeError):
                pub_date = timezone.now()

            obj, created = Article.objects.get_or_create(
                title=item.get('title', ''),
                defaults={
                    'category': category_key,
                    'summary': item.get('summary', ''),
                    'content': item.get('content', ''),
                    'status': True,
                    'published_at': pub_date,
                },
            )
            if created:
                self.stdout.write(f'  ✓ 新闻: {item["title"]}')
            else:
                self.stdout.write(f'  - 新闻已存在，跳过: {item["title"]}')
