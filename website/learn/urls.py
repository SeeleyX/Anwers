from django.contrib import admin
from django.urls import path, include
from learn import views

app_name = 'learn'

urlpatterns = [
	path('', views.learn_base, name="learn_base"),
	path('astronomy/', views.astronomy, name='astronomy'),
]