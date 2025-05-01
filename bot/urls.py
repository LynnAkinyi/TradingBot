from django.urls import path
from . import views

urlpatterns = [
    path('', views.bot_list, name='bot_list'),
    path('create/', views.bot_create, name='bot_create'),
    path('start/<int:bot_id>/', views.bot_start, name='bot_start'),
    path('stop/<int:bot_id>/', views.bot_stop, name='bot_stop'),
]