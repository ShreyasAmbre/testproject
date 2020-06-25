from django.urls import path
from calc import views
urlpatterns = [
    path('home/', views.home, name="home"),
    path('home/add', views.add, name="add"),
    # path('add/', views.add, name="add"),
]