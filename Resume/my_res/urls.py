from django.contrib import admin
from django.urls import path, include
from my_res import views
from django.views.static import serve
from django.conf.urls import url
from django.conf import settings

urlpatterns = [
    path('',views.index,name='my_res'),
    path('project/',views.project,name='my_res'),
    path('contact/',views.contact,name='my_res'),
    path('certificate/',views.certificate,name='my_res'),
    path('cv/',views.cv,name='my_res'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 

]