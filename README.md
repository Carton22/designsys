# 项目说明

### 部署方法
1. 安装基础环境
```
pip install -r requirements.txt
```

2. 初始化数据库
```
python manage.py makemigrations
python manage.py migrate
```

3. 安装redis
3. 在另一个终端同步运行

```
redis-server
```

5. 运行项目

```
python manage.py runserver
```

6. 进入网址：http://127.0.0.1:8000/

### 运行效果 

可在多个网页同步显示文字

### 待实现功能

前端界面优化

图片同步显示

数据文件暂存中转