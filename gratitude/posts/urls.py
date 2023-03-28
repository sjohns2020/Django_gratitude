from . import views
from django.urls import path

urlpatterns = [
    path('', views.list, name='posts'),
    path('dashboard/', views.dashboard, name='dashboard')
]