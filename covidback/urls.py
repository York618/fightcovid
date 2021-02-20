from django.urls import include,path

from . import views

app_name = 'covidback'
urlpatterns = [
    path('' , views.index, name='index'),
    path('index/', views.index, name='index'),
    path('video/', views.videoindex, name='video'),
    path('video/1', views.video1, name='video1'),
    path('video/2', views.video2, name='video2'),
    path('overview/', views.overview, name='overview'),
]
