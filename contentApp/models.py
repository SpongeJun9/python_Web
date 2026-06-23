from django.db import models
from django.utils import timezone


class Article(models.Model):
    CATEGORY_CHOICES = (
        ('notice', '战队公告'),
        ('competition', '赛事动态'),
        ('training', '训练记录'),
        ('tech', '技术文章'),
        ('recruit', '招新信息'),
        ('cooperation', '合作交流'),
        ('achievement', '成果展示'),
    )
    title = models.CharField('标题', max_length=150)
    category = models.CharField('分类', max_length=30, choices=CATEGORY_CHOICES, default='notice')
    cover_image = models.ImageField('封面图', upload_to='articles/', blank=True)
    summary = models.TextField('摘要', max_length=300, blank=True)
    content = models.TextField('正文')
    author = models.CharField('作者', max_length=50, default='LionHeart')
    tags = models.CharField('标签', max_length=120, blank=True)
    view_count = models.IntegerField('阅读量', default=0)
    is_top = models.BooleanField('是否置顶', default=False)
    is_recommend = models.BooleanField('是否推荐', default=False)
    status = models.BooleanField('是否发布', default=True)
    published_at = models.DateTimeField('发布时间', default=timezone.now)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = '新闻文章'
        verbose_name_plural = '新闻文章'
        ordering = ['-is_top', '-published_at']

    def __str__(self):
        return self.title


class RobotProject(models.Model):
    name = models.CharField('机器人名称', max_length=80)
    robot_type = models.CharField('机器人类型', max_length=80, blank=True)
    cover_image = models.ImageField('封面图', upload_to='robots/', blank=True)
    description = models.TextField('功能定位')
    technical_features = models.TextField('技术特点', blank=True, help_text='可按行填写')
    hardware_config = models.TextField('硬件配置', blank=True)
    software_config = models.TextField('软件配置', blank=True)
    progress = models.CharField('研发进度', max_length=80, blank=True)
    video_url = models.URLField('演示视频', blank=True)
    status = models.BooleanField('是否展示', default=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = '机器人项目'
        verbose_name_plural = '机器人项目'
        ordering = ['id']

    def __str__(self):
        return self.name

    def feature_list(self):
        return [item.strip() for item in self.technical_features.splitlines() if item.strip()]


class RobotImg(models.Model):
    """机器人图片 - 支持多图上传"""
    robot = models.ForeignKey(
        RobotProject,
        related_name='robotImgs',
        verbose_name='机器人',
        on_delete=models.CASCADE
    )
    photo = models.ImageField('机器人图片', upload_to='robots/')
    description = models.CharField('图片描述', max_length=200, blank=True)
    order = models.IntegerField('排序', default=0)

    class Meta:
        verbose_name = '机器人图片'
        verbose_name_plural = '机器人图片'
        ordering = ['order', 'id']

    def __str__(self):
        return f'{self.robot.name} - 图片{self.id}'


class Achievement(models.Model):
    competition_name = models.CharField('比赛名称', max_length=120)
    award_level = models.CharField('获奖等级', max_length=80, blank=True)
    project_name = models.CharField('项目名称', max_length=120, blank=True)
    award_time = models.DateField('获奖时间', blank=True, null=True)
    members = models.CharField('参赛成员', max_length=200, blank=True)
    teacher = models.CharField('指导老师', max_length=100, blank=True)
    description = models.TextField('成果说明', blank=True)
    certificate_image = models.ImageField('证书图片', upload_to='achievements/', blank=True)
    status = models.BooleanField('是否展示', default=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = '赛事成果'
        verbose_name_plural = '赛事成果'
        ordering = ['-award_time', '-created_at']

    def __str__(self):
        return self.competition_name
