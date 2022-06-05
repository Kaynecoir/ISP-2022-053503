from django.urls import path
from . import views


urlpatterns = [

 path('', views.home, name="home"),
 path('track-create/', views.TrackCreate.as_view(), name="track-create"),
 path('track-update/<int:pk>/', views.TrackUpdate.as_view(), name="track-update"),
 path('track-delete/<int:pk>/', views.TrackDelete.as_view(), name="track-delete"),
 path('../musics/a.mp3', views.TrackDetail.as_view(), name='track-play'),
 path('signup/', views.SignUp.as_view(), name='signup'),
 path('about/', views.AboutSite.as_view(), name='about'),


]