# howdy/urls.py
from django.conf.urls import url
from .views import check_med
from summarizer import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   url(r'$', check_med),
   # url(r'^about/$', views.about, name='about'),
   ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)