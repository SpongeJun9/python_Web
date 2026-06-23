from django.shortcuts import render

from contentApp.models import Achievement, Article, RobotProject
from . import data
from .models import Carousel, Member, Resource, Sponsor


def home(request):
    robots = RobotProject.objects.filter(status=True)[:4]
    articles = Article.objects.filter(status=True)[:3]
    achievements = Achievement.objects.filter(status=True)[:3]
    carousels = Carousel.objects.filter(status=True, page='home')

    return render(request, 'home.html', {
        'robots': robots,
        'articles': articles,
        'achievements': achievements,
        'carousels': carousels,
        'default_robots': data.ROBOTS[:4],
        'default_news': data.NEWS,
        'default_achievements': data.ACHIEVEMENTS,
        'directions': data.DIRECTIONS,
        'team_name': data.TEAM_NAME,
        'slogan': data.SLOGAN,
        'sub_slogan': data.SUB_SLOGAN,
    })


def about(request):
    leader = Member.objects.filter(status=True, position='战队负责人').first()
    carousels = Carousel.objects.filter(status=True, page='about')
    return render(request, 'about.html', {
        'values': data.VALUES,
        'roadmap': data.ROADMAP,
        'leader': leader,
        'carousels': carousels,
    })


def robomaster(request):
    return render(request, 'robomaster.html')


def technical(request):
    return render(request, 'technical.html', {
        'directions': data.DIRECTIONS,
    })


def members(request):
    members_qs = Member.objects.filter(status=True)
    return render(request, 'members.html', {
        'members': members_qs,
        'organization': data.ORGANIZATION,
        'directions': data.DIRECTIONS,
    })


def sponsor(request):
    sponsors = Sponsor.objects.filter(status=True)
    return render(request, 'sponsor.html', {'sponsors': sponsors})


def resources(request):
    resources_qs = Resource.objects.filter(status=True)
    return render(request, 'resources.html', {
        'resources': resources_qs,
        'default_resources': data.RESOURCES,
    })


def contact(request):
    return render(request, 'contact.html')
