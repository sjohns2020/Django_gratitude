from . import views
from django.urls import path

urlpatterns = [
    path('', views.list, name='posts'),
    path('new/', views.post_new, name='post_new'),
    path('dashboard/', views.dashboard, name='dashboard')
]