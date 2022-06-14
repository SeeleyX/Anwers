from django.contrib import admin
from django.urls import path, include
from learn import views

app_name = 'learn'

urlpatterns = [
	path('', views.index, name='index'),
]