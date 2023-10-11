# In Settings.py : 

STATIC_URL = 'static/'
MEDIA_URL = 'media/'
STATICFILES_DIRS = [BASE_DIR / 'static', ]
MEDIA_ROOT = BASE_DIR / 'media'

# in Project urls.py:

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    # email varifikeson 
    
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_BackEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "your gmail"
EMAIL_HOST_PASSWORD = "your password "

# project file creat
py -m venv env

env\Scripts\activate

django-admin startproject ( project name )

pip install django

python manage.py makemigrations

python manage.py migrate

python manage.py runserver 
python manage.py createsuperuser

python manage.py startapp  (  app name )

pip install pillow

# google login 
pip install django-allauth(All-Auth Social Login Authentication | API inastall )

# html templet pdf convart
pip install xhtml2pdf

# admin penel chans
pip install django_jazzmin