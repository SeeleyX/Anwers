from re import template
# from unittest import loader
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from django.template import loader

def index(request):
	context_dict = {}
	return render(request, 'learn/index.html', context=context_dict)

def astronomy(request):
	context_dict = {}
	return render(request, 'learn/astronomy.html', context=context_dict)



def maths(request):
	context_dict = {}
	return render(request, 'learn/maths.html', context=context_dict)


def physics(request):
	context_dict = {
		'topic_title':'Physics'
	}
	return render(request, 'learn/topic.html', context=context_dict)


def learn_base(request):
	return redirect("/")

def maths_linear_algebra(request):
	context_dict = {
		'sub_topic_title': 'Linear Algebra',
	}
	return render(request, 'learn/sub-topic.html', context=context_dict)
