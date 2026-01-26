
from .base import *

DEBUG = False

ALLOWED_HOSTS = ["*"]
# ALLOWED_HOSTS = [
#     ".elasticbeanstalk.com",
#     "hireiq-prod.eba-mrwhgqww.ap-south-1.elasticbeanstalk.com",
# ]

SECURE_SSL_REDIRECT = False
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SECURE_HSTS_SECONDS = 60 * 60 * 24
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = False

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"