import imp
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib import settings
# from django.contrib.staticfiles import static
urlpatterns=[
    path('',views.index,name='index'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('posts/<str:pk>',views.posts,name='posts')

]
if settings.DEBUG :
    urlpatterns +=static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT )
