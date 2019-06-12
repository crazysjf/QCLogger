# 部署

安装：
pip install Django
pip install uwsgi

./manage.py migrate

此时运行
./manage.py runserver
应该可以运行服务器

需要创建超级用户:

./manage.py createsuperuser

此时可以用刚创建的超级用户登录管理界面：/admin