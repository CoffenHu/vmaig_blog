# -*- coding: utf-8 -*-
"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.8.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p1p2e^77+6ex*1@-s6hzcx7l3bx#g2q0w1za1c-x-1p@n6z^x*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',

    'blog',
    'vmaig_auth',
    'vmaig_comments',
    'vmaig_system'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'vmaig_blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [os.path.join(BASE_DIR, "templates/")],
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'vmaig_blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

# 设置user model
AUTH_USER_MODEL = "vmaig_auth.VmaigUser"


# log配置
LOG_FILE = "./all.log"

LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,

        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
                }
            },
        'formatters': {
            'simple': {
                'format': '[%(levelname)s] %(module)s : %(message)s'
                },
            'verbose': {
                'format':
                    '[%(asctime)s] [%(levelname)s] %(module)s : %(message)s'
                }
            },

        'handlers': {
            'null': {
                'level': 'DEBUG',
                'class': 'django.utils.log.NullHandler',
                },
            'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
                },
            'file': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'formatter': 'verbose',
                'filename': LOG_FILE,
                'mode': 'a',
                },
            'mail_admins': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler',
                'filters': ['require_debug_false']
                }
            },
        'loggers': {
            '': {
                'handlers': ['file', 'console'],
                'level': 'INFO',
                'propagate': True,
                },
            'django': {
                'handlers': ['file', 'console'],
                'level': 'DEBUG',
                'propagate': True,
                },
            'django.request': {
                'handlers': ['mail_admins', 'console'],
                'level': 'ERROR',
                'propagate': True,
                },
            }
        }


# cache配置
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
        'options': {
            'MAX_ENTRIES': 1024,
        }
    },
    'memcache': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        # 'LOCATION': 'unix:/home/billvsme/memcached.sock',
        'LOCATION': '127.0.0.1:11211',
        'options': {
            'MAX_ENTRIES': 1024,
        }
    },
}


# 分页配置
PAGE_NUM = 5

# email配置
# 如果想要支持ssl (比如qq邮箱) 见 https://github.com/bancek/django-smtp-ssl
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = ''                       # SMTP地址 例如: smtp.163.com
EMAIL_PORT = 25                       # SMTP端口 例如: 25
EMAIL_HOST_USER = ''                  # 我自己的邮箱 例如: xxxxxx@163.com
EMAIL_HOST_PASSWORD = ''              # 我的邮箱密码 例如  xxxxxxxxx
EMAIL_SUBJECT_PREFIX = u'vmaig'       # 为邮件Subject-line前缀,默认是'[django]'
EMAIL_USE_TLS = True                  # 与SMTP服务器通信时，是否启动TLS链接(安全链接)。默认是false

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# 七牛配置
QINIU_ACCESS_KEY = ''
QINIU_SECRET_KEY = ''
QINIU_BUCKET_NAME = ''
QINIU_URL = ''

# 网站标题等内容配置
WEBSITE_TITLE = u'TuTu'
WEBSITE_WELCOME = u'欢迎来到TuTu'

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

SUIT_CONFIG = {
    'ADMIN_NAME': u'TuTu后台管理平台',
    'HEADER_DATE_FORMAT': 'Y年 F j日 l',
    'HEADER_TIME_FORMAT': 'H:i',
    'SHOW_REQUIRED_ASTERISK': True,
    'CONFIRM_UNSAVED_CHANGES': True,
    'SEARCH_URL': '/admin/blog/article/',
    'MENU_OPEN_FIRST_CHILD': True,
    'LIST_PER_PAGE': 50,
    'MENU': (
        # 'sites',
        # {'app': 'blog', 'label': u'博客', 'icon': 'icon-lock'},
        # # Rename app and set icon
        # {'app': 'auth', 'label': 'Authorization', 'icon':'icon-lock'},
        #
        # # Reorder app models
        # {'app': 'auth', 'models': ('user', 'group')},
        #
        # # Custom app, with models
        # {'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
        #
        # # Cross-linked models with custom name; Hide default icon
        # {'label': 'Custom', 'icon':None, 'models': (
        #     'auth.group',
        #     {'model': 'auth.user', 'label': 'Staff'}
        # )},
        #
        # # Custom app, no models (child links)
        # {'label': 'Users', 'url': 'auth.user', 'icon':'icon-user'},
        #
        # # Separator
        # '-',
        #
        # # Custom app and model with permissions
        # {'label': 'Secure', 'permissions': 'auth.add_user', 'models': [
        #     {'label': 'custom-child', 'permissions': ('auth.add_user', 'auth.add_group')}
        # ]},

        # {'label': u'参数配置', 'icon': 'icon-user', 'models': (
        #
        #     {'model': 'common.ParaElec', 'label': u'电力热力排放因子配置'},
        #     # {'model': 'common.ParaQushi', 'label': u'变暖潜势配置'},
        #     {'model': 'provincial.DeadlineActivity', 'label': u'截至日期配置'},
        #     {'model': 'common.CommonSourceFueltype', 'label': u'原料类型'},
        #     {'model': 'common.IndustryGlobaWarmingTrend', 'label': u'全球变暖潜势配置'},
        #     {'model': 'common.IndustrySpecialConf', 'label': u'行业特殊配置'},
        #
        #     {'model': 'industry.IndustryElectronicMadeProcessVal1', 'label': u'电子设备制造行业-过程排放-原料气配置'},
        #     {'model': 'industry.IndustryElectronicMadeProcessValName', 'label': u'电子设备制造行业-过程排放-副产品配置'},
        #     {'model': 'industry.IndustryElectronicMadeProcessValRelate', 'label': u'电子设备制造行业-过程排放数据配置'},
        #     {'model': 'companysource.CompanySourceLandCH4', 'label': u'陆上交通运输-N20、CH4排放因子配置'},
        #
        #     {'model': 'common.region', 'label': u'市区配置'},
        #     {'model': 'common.SecordRegion', 'label': u'地区配置'},
        #     {'model': 'common.BusinessType', 'label': u'企业用户类型配置'},
        # )},
        # {'label': u'数据库导出配置', 'icon': 'icon-user', 'models': (
        #     {'model': 'provincial.DataBaseTableGroup', 'label': u'数据库基础配置'},
        #     {'model': 'provincial.DatabaseExport', 'label': u'数据库导出配置'},
        # )},
        # {'label': u'用户', 'icon': 'icon-user', 'models': (
        #     {'model': 'user.AuthorityGroup', 'label': u'权限组'},
        #     {'model': 'provincial.CommonUser', 'label': u'用户管理'},
        # )}
    )
}