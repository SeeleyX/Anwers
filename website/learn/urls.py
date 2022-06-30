from django.contrib import admin
from django.urls import path, include
from learn import views

app_name = 'learn'

urlpatterns = [
	path('', views.learn_base, name="learn_base"),
	path('index', views.learn_base, name='index'),
	path('astronomy/', views.astronomy, name='astronomy'),
	path('login/', views.user_login, name='user_login'),
	path('register/', views.user_register, name='user_register'),
]
