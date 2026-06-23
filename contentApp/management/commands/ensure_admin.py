"""
创建或重置默认管理员账号。
运行方式: python manage.py ensure_admin
"""
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = '确保存在一个管理员账号，密码为 admin123'

    def handle(self, *args, **options):
        username = 'admin'
        password = 'admin123'

        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            user.set_password(password)
            user.is_superuser = True
            user.is_staff = True
            user.save()
            self.stdout.write(self.style.SUCCESS(f'管理员密码已重置: {username} / {password}'))
        else:
            User.objects.create_superuser(username, '', password)
            self.stdout.write(self.style.SUCCESS(f'管理员已创建: {username} / {password}'))
