from django.contrib import admin
from django.urls import path, include
from learn import views

app_name = 'learn'

urlpatterns = [
	path('', views.learn_base, name="learn_base"),
	path('physics/', views.physics, name='physics'),
	path('compSci/', views.compSci, name='compSci'),
	path('maths/', views.maths, name='maths'),
]