from django.contrib import admin
from django.urls import path, include
from learn import views

app_name = 'learn'

urlpatterns = [
	path('', views.index, name='index'),
	path('john/', views.run_john, name='run_john')
]