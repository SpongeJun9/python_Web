from django.contrib import admin
from .models import Achievement, Article, RobotProject, RobotImg


class RobotImgInline(admin.StackedInline):
    """机器人图片内联编辑"""
    model = RobotImg
    extra = 1
    fields = ('photo', 'description', 'order')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'view_count', 'is_top', 'is_recommend', 'status', 'published_at')
    list_filter = ('category', 'is_top', 'is_recommend', 'status', 'published_at')
    search_fields = ('title', 'summary', 'content', 'tags', 'author')
    list_editable = ('is_top', 'is_recommend', 'status')
    date_hierarchy = 'published_at'
    readonly_fields = ('view_count', 'created_at', 'updated_at')
    fieldsets = (
        ('基本信息', {
            'fields': ('title', 'category', 'author', 'tags')
        }),
        ('内容', {
            'fields': ('summary', 'content', 'cover_image')
        }),
        ('状态', {
            'fields': ('is_top', 'is_recommend', 'status', 'published_at')
        }),
        ('统计', {
            'fields': ('view_count', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(RobotProject)
class RobotProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'robot_type', 'progress', 'status', 'created_at')
    list_filter = ('robot_type', 'status', 'created_at')
    search_fields = ('name', 'description', 'technical_features', 'hardware_config', 'software_config')
    list_editable = ('status',)
    readonly_fields = ('created_at', 'updated_at')
    inlines = [RobotImgInline]
    fieldsets = (
        ('基本信息', {
            'fields': ('name', 'robot_type', 'cover_image', 'status')
        }),
        ('功能描述', {
            'fields': ('description', 'technical_features')
        }),
        ('配置信息', {
            'fields': ('hardware_config', 'software_config', 'progress')
        }),
        ('其他', {
            'fields': ('video_url', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('competition_name', 'award_level', 'project_name', 'award_time', 'status')
    list_filter = ('award_level', 'status', 'award_time')
    search_fields = ('competition_name', 'project_name', 'members', 'teacher', 'description')
    list_editable = ('status',)
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'award_time'
