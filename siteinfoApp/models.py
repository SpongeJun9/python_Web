from django.db import models


class Carousel(models.Model):
    """轮播图 - 支持多页面"""
    PAGE_CHOICES = (
        ('home', '首页'),
        ('about', '关于战队'),
    )
    page = models.CharField('所属页面', max_length=30, choices=PAGE_CHOICES, default='home')
    title = models.CharField('标题', max_length=100, blank=True, help_text='轮播图标题，可选')
    subtitle = models.CharField('副标题', max_length=200, blank=True, help_text='轮播图副标题，可选')
    image = models.ImageField('轮播图片', upload_to='carousel/')
    link_url = models.URLField('链接地址', blank=True, help_text='点击图片跳转的链接，可选')
    order = models.IntegerField('排序', default=0, help_text='数字越小越靠前')
    status = models.BooleanField('是否展示', default=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = '轮播图'
        ordering = ['page', 'order', 'id']

    def __str__(self):
        return self.title if self.title else f'轮播图 {self.id}'


class SiteConfig(models.Model):
    config_key = models.CharField('配置键', max_length=80, unique=True)
    config_value = models.TextField('配置值')
    description = models.CharField('说明', max_length=200, blank=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = '网站配置'
        verbose_name_plural = '网站配置'

    def __str__(self):
        return self.config_key


class Member(models.Model):
    name = models.CharField('姓名', max_length=30)
    gender = models.CharField('性别', max_length=10, blank=True)
    college = models.CharField('学院', max_length=80, blank=True)
    major = models.CharField('专业', max_length=80, blank=True)
    grade = models.CharField('年级', max_length=20, blank=True)
    group_name = models.CharField('方向组', max_length=50)
    position = models.CharField('职位', max_length=50, blank=True)
    description = models.TextField('个人简介', blank=True)
    avatar = models.ImageField('照片', upload_to='members/', blank=True)
    github_url = models.URLField('GitHub/Gitee', blank=True)
    bilibili_url = models.URLField('B站链接', blank=True)
    status = models.BooleanField('是否展示', default=True)
    sort_order = models.IntegerField('排序', default=0)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = '成员'
        verbose_name_plural = '成员'
        ordering = ['sort_order', 'id']

    def __str__(self):
        return self.name


class Sponsor(models.Model):
    company_name = models.CharField('合作方名称', max_length=100)
    logo = models.ImageField('Logo', upload_to='sponsors/', blank=True)
    cooperation_type = models.CharField('合作类型', max_length=80, blank=True)
    description = models.TextField('合作说明', blank=True)
    sponsor_level = models.CharField('赞助等级', max_length=50, blank=True)
    website_url = models.URLField('官网链接', blank=True)
    contact_person = models.CharField('联系人', max_length=50, blank=True)
    status = models.BooleanField('是否展示', default=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = '合作赞助'
        verbose_name_plural = '合作赞助'

    def __str__(self):
        return self.company_name


class Resource(models.Model):
    PERMISSION_CHOICES = (
        ('public', '公开资料'),
        ('member', '成员资料'),
        ('internal', '内部资料'),
    )
    title = models.CharField('标题', max_length=120)
    category = models.CharField('分类', max_length=50)
    file_url = models.FileField('资源文件', upload_to='resources/', blank=True)
    external_url = models.URLField('外部链接', blank=True)
    description = models.TextField('简介', blank=True)
    permission_level = models.CharField('权限等级', max_length=20, choices=PERMISSION_CHOICES, default='public')
    download_count = models.IntegerField('下载次数', default=0)
    status = models.BooleanField('是否展示', default=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = '资源文件'
        verbose_name_plural = '资源文件'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
