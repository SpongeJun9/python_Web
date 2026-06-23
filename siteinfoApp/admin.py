from django.contrib import admin
from .models import Carousel, Member, Resource, SiteConfig, Sponsor


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ('title', 'page', 'order', 'status', 'created_at')
    list_filter = ('page', 'status', 'created_at')
    search_fields = ('title', 'subtitle')
    list_editable = ('page', 'order', 'status')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('基本信息', {
            'fields': ('title', 'subtitle', 'image')
        }),
        ('设置', {
            'fields': ('link_url', 'order', 'status')
        }),
        ('时间信息', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    list_display = ('config_key', 'description', 'updated_at')
    search_fields = ('config_key', 'description')


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'group_name', 'position', 'college', 'grade', 'status', 'sort_order')
    list_filter = ('group_name', 'status', 'grade')
    search_fields = ('name', 'college', 'major', 'group_name', 'position')
    list_editable = ('status', 'sort_order')


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'cooperation_type', 'sponsor_level', 'contact_person', 'status', 'created_at')
    list_filter = ('cooperation_type', 'sponsor_level', 'status')
    search_fields = ('company_name', 'description', 'contact_person')


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'permission_level', 'download_count', 'status', 'created_at')
    list_filter = ('category', 'permission_level', 'status')
    search_fields = ('title', 'description')
