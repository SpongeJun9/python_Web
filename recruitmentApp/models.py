from django.db import models


class RecruitmentApplication(models.Model):
    STATUS_CHOICES = (
        ('submitted', '已提交'),
        ('screening', '初筛中'),
        ('interview', '面试/答辩'),
        ('accepted', '已录取'),
        ('rejected', '未通过'),
    )

    name = models.CharField('姓名', max_length=30)
    gender = models.CharField('性别', max_length=10, blank=True)
    college = models.CharField('学院', max_length=80)
    major = models.CharField('专业', max_length=80)
    grade = models.CharField('年级', max_length=20)
    phone = models.CharField('手机号', max_length=30)
    qq = models.CharField('QQ', max_length=30, blank=True)
    wechat = models.CharField('微信', max_length=50, blank=True)
    email = models.EmailField('邮箱', blank=True)
    target_group = models.CharField('意向方向', max_length=80)
    has_basic = models.CharField('是否有基础', max_length=20, blank=True)
    skills = models.TextField('掌握技能', blank=True)
    experience = models.TextField('项目或比赛经历', blank=True)
    reason = models.TextField('加入理由')
    available_time = models.CharField('每周可投入时间', max_length=80, blank=True)
    accept_assessment = models.BooleanField('是否接受考核', default=True)
    attachment = models.FileField('附件', upload_to='applications/', blank=True)
    status = models.CharField('处理状态', max_length=20, choices=STATUS_CHOICES, default='submitted')
    remark = models.TextField('后台备注', blank=True)
    created_at = models.DateTimeField('提交时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = '招新报名'
        verbose_name_plural = '招新报名'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} - {self.target_group}'
