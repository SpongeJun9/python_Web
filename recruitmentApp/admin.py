from django.contrib import admin
from .models import RecruitmentApplication


@admin.register(RecruitmentApplication)
class RecruitmentApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'college', 'major', 'grade', 'target_group', 'phone', 'status', 'created_at')
    list_filter = ('target_group', 'grade', 'status', 'created_at')
    search_fields = ('name', 'college', 'major', 'phone', 'qq', 'wechat', 'skills', 'reason')
    list_editable = ('status',)
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'
    fieldsets = (
        ('基本信息', {
            'fields': ('name', 'college', 'major', 'grade')
        }),
        ('报名意向', {
            'fields': ('target_group', 'skills', 'reason')
        }),
        ('联系方式', {
            'fields': ('phone', 'qq', 'wechat', 'email')
        }),
        ('状态管理', {
            'fields': ('status', 'created_at', 'updated_at')
        }),
    )
