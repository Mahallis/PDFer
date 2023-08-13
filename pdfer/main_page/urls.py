from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/<str:name>/', views.names, name='names'),

]
