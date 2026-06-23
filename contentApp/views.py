from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from siteinfoApp import data
from .models import Achievement, Article, RobotProject


def robots(request):
    robot_list = RobotProject.objects.filter(status=True)

    # 为每个机器人关联第一张图片
    for robot in robot_list:
        if robot.robotImgs.exists():
            robot.first_image = robot.robotImgs.first()

    return render(request, 'robots.html', {
        'robots': robot_list,
        'default_robots': data.ROBOTS,
    })


def robot_detail(request, pk):
    robot = get_object_or_404(RobotProject, pk=pk, status=True)

    # 获取所有图片
    images = robot.robotImgs.all()

    return render(request, 'robot_detail.html', {
        'robot': robot,
        'images': images,
    })


def robot_default_detail(request, slug):
    robot = next((item for item in data.ROBOTS if item['slug'] == slug), None)
    if robot is None:
        robot = data.ROBOTS[0]
    return render(request, 'robot_detail.html', {'default_robot': robot})


def achievements(request):
    achievement_list = Achievement.objects.filter(status=True)
    return render(request, 'achievements.html', {
        'achievements': achievement_list,
        'default_achievements': data.ACHIEVEMENTS,
    })


def news(request):
    """新闻列表 - 支持分类和分页"""
    category = request.GET.get('category', '')

    # 根据分类筛选
    if category:
        articles = Article.objects.filter(status=True, category=category)
    else:
        articles = Article.objects.filter(status=True)

    # 分页
    paginator = Paginator(articles, 10)
    page = request.GET.get('page', 1)

    try:
        articles_page = paginator.page(page)
    except PageNotAnInteger:
        articles_page = paginator.page(1)
    except EmptyPage:
        articles_page = paginator.page(paginator.num_pages)

    return render(request, 'news.html', {
        'articles': articles_page,
        'default_news': data.NEWS,
        'current_category': category,
        'paginator': paginator,
    })


def news_detail(request, pk):
    """新闻详情 - 增加浏览量"""
    article = get_object_or_404(Article, pk=pk, status=True)

    # 增加浏览量
    Article.objects.filter(pk=pk).update(view_count=article.view_count + 1)
    article.refresh_from_db()

    return render(request, 'news_detail.html', {'article': article})


def news_default_detail(request, slug):
    article = next((item for item in data.NEWS if item['slug'] == slug), None)
    if article is None:
        article = data.NEWS[0]
    return render(request, 'news_detail.html', {'default_article': article})


def news_search(request):
    """新闻搜索"""
    keyword = request.GET.get('keyword', '').strip()

    if keyword:
        articles = Article.objects.filter(
            Q(title__icontains=keyword) |
            Q(content__icontains=keyword) |
            Q(summary__icontains=keyword) |
            Q(tags__icontains=keyword),
            status=True
        )
    else:
        articles = Article.objects.filter(status=True)

    # 分页
    paginator = Paginator(articles, 10)
    page = request.GET.get('page', 1)

    try:
        articles_page = paginator.page(page)
    except PageNotAnInteger:
        articles_page = paginator.page(1)
    except EmptyPage:
        articles_page = paginator.page(paginator.num_pages)

    return render(request, 'news_search.html', {
        'articles': articles_page,
        'keyword': keyword,
        'paginator': paginator,
    })
