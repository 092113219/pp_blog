from .base import *

DEBUG = True

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',   #数据库名
        'USER': 'root',    #用户名
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'CHARSET': 'utf8',##设置字符集，不然会出现中文乱码
        'TEST': {
            'NAME': 'student_test',
        },
    },
}