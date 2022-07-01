from django.contrib import admin
from django.urls import path, include
from learn import views

app_name = 'learn'

urlpatterns = [
	path('', views.learn_base, name="learn_base"),
	path('maths/', views.maths, name='maths'),
	path('computerScience/', views.computerScience, name='computerScience'),
	path('physics/', views.physics, name='physics'),
	path('maths/linear_algebra', views.maths_linear_algebra, name='linear algebra'),
]