from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

def index(request):
	context_dict = {}
	return render(request, 'learn/index.html', context=context_dict)

def astronomy(request):
	context_dict = {}
	return render(request, 'learn/astronomy.html', context=context_dict)

def physics(request):
	context_dict = {}
	return render(request, 'learn/physics.html', context=context_dict)

def maths(request):
	context_dict = {}
	return render(request, 'learn/maths.html', context=context_dict)

def learn_base(request):
	return redirect("/")