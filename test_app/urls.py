from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'upload', views.upload_image, name='upload_image'),
  url(r'', views.index, name='index'),
]