from django.urls import path
from . import views
urlpatterns = [
    path('', views.zomato, name='home'),
    path('zomato2/', views.zomato2, name='zomato2'),
]