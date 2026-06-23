# LionHeart 机器人战队官方网站

这是根据原 hengDaProject 教学项目所使用的 Django 技术栈重新编写的 LionHeart 官网，代码仅放在当前 LionHeart 目录内。

## 技术栈

- Django 3.2
- SQLite
- 多 App 拆分
- Django Templates 模板继承
- Bootstrap 3 + jQuery + Bootstrap JS
- 自定义蓝白明亮科技风 CSS
- Django Admin 后台管理
- ModelForm 招新报名表

## App 划分

- siteinfoApp：首页、关于战队、RoboMaster、技术方向、成员组织、合作赞助、资源中心、联系我们
- contentApp：机器人阵容、赛事成果、新闻动态
- recruitmentApp：招新报名表与报名数据管理

## 启动方式

1. pip install -r requirements.txt
2. 复制 `.env.example` 到 `.env`，并填写 `DEEPSEEK_API_KEY`
3. python manage.py migrate
4. python manage.py createsuperuser
5. python manage.py runserver

访问：

- 官网首页：http://127.0.0.1:8000/
- 后台管理：http://127.0.0.1:8000/admin/

页面内置了完整的样例展示数据。后台录入真实数据后，列表页会优先显示数据库内容。
