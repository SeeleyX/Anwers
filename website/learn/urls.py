from django.contrib import admin
from django.urls import path, include
from learn import views

app_name = 'learn'

urlpatterns = [
	path('', views.learn_base, name="learn_base"),
	path('index/', views.learn_base, name='index'),
	path('login/', views.user_login, name='user_login'),
	path('register/', views.user_register, name='user_register'),
	path('maths/', views.maths, name='maths'),
	path('astronomy/', views.astronomy, name='astronomy'),
	path('physics/', views.physics, name='physics'),
	path('maths/linear_algebra', views.maths_linear_algebra, name='linear algebra'),
]
