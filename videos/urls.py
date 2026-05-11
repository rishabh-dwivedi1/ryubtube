from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('upload/', views.upload_video, name='upload'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('watch/<int:video_id>/', views.watch_video, name='watch_video'),
    path('like/<int:video_id>/', views.like_video, name='like_video'),
    path('search/', views.search, name='search'),
]