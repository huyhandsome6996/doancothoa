"""
Cấu hình Django cho dự án DOANCOTHOA (App Thu Ngân Online).
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-thay-bang-key-bi-mat-cua-ban'

# SECURITY WARNING: don't run with debug turned on in production!
# Khi deploy lên Render, hãy đổi thành False
DEBUG = True

# Cho phép các domain nào được truy cập vào Backend (dấu '*' nghĩa là cho phép tất cả)
ALLOWED_HOSTS = ['*'] 


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # --- THƯ VIỆN CÀI THÊM CỦA CHÚNG TA ---
    'corsheaders',      # Xử lý lỗi CORS khi Frontend gọi API
    'rest_framework',   # Hỗ trợ xây dựng API mạnh mẽ
    'dangnhap'
]

MIDDLEWARE = [
    # Middleware của corsheaders PHẢI được đặt ở trên CommonMiddleware
    'corsheaders.middleware.CorsMiddleware',
    
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# Mặc định dùng SQLite cho lúc lập trình.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
LANGUAGE_CODE = 'vi' # Chuyển ngôn ngữ sang Tiếng Việt
TIME_ZONE = 'Asia/Ho_Chi_Minh' # Chuyển múi giờ về Việt Nam
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # Cần thiết cho Render

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# --- CẤU HÌNH CORS CHO FRONTEND ---
# Cho phép Frontend từ bất kỳ tên miền nào cũng gọi được API (Thích hợp lúc dev)
CORS_ALLOW_ALL_ORIGINS = True

# --- CẤU HÌNH REST FRAMEWORK (Tùy chọn cơ bản) ---
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
}