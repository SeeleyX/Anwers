from re import template
# from unittest import loader
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from django.template import loader


def index(request):
	context_dict = {}
	return render(request, 'learn/index.html', context=context_dict)

def physics(request):
	context_dict = {

		'topic_title': 'Physics',
		'topic': 1,
		'index': 'phys',

		'sub_topics': [
		{
        'title': 'Thermal Physics',
        'image': 'Thermal',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
      	},
      	{
        'title': 'Newtonian Dynamics',
        'image': 'Newtonian',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
     	},
      	{
        'title': 'Oscillating Systems',
        'image': 'Oscillating_Systems',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
      	},
      	{
        'title': 'Electricity and Magnetism',
        'image': 'Electricity',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
      	},
      	{
        'title': 'Physics of Solids',
        'image': 'POS',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
      	},
      	{
        'title': 'Nuclear and Particle Physics',
        'image': 'NPP',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
     	},
      	{
        'title': 'Optics',
        'image': 'Optics',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
      	},
      	{
        'title': 'Quantum and Classical Waves',
        'image': 'Quantum_Waves',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
      	}]
	}
	return render(request, 'learn/topic.html', context=context_dict)


def maths(request):
	context_dict = {

		'topic_title': 'Maths',
		'topic': 2,
		'index': 'maths',

		'sub_topics': [
		{
        'title': 'Linear Algebra',
        'image': 'Linear_Algebra',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
      	},
      	{
        'title': 'Abstract Algebra and Groups',
        'image': 'Abstract_Algebra',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
     	},
      	{
        'title': 'Real Analysis',
        'image': 'Real_Analysis',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
      	},
      	{
        'title': 'Multivariable Calculus',
        'image': 'Multivariable_Calculus',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
      	},
      	{
        'title': 'Mechanics',
        'image': 'Mechanics',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
      	},
      	{
        'title': 'Mathimatical Methods & Modelling',
        'image': 'Mathematical_Models',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
     	}]
	}
	return render(request, 'learn/topic.html', context=context_dict)


def computerScience(request):
	context_dict = {

		'topic_title': 'Computer Science',
		'topic': 3,
		'index': 'comp',

		'sub_topics': [
		{
        'title': 'Text as Data',
        'image': 'Linear_Algebra',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
      	},
      	{
        'title': 'Programming Languages',
        'image': 'Programming_Languages',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
     	},
      	{
        'title': 'Data-Fundementals',
        'image': 'Real_Analysis',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
      	},
      	{
        'title': 'Algorithmics',
        'image': 'Multivariable_Calculus',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
      	}]
	}
	return render(request, 'learn/topic.html', context=context_dict)



def learn_base(request):
	return redirect("/")


def maths_linear_algebra(request):
	context_dict = {
		'sub_topic_title': 'Linear Algebra',
	}
	return render(request, 'learn/sub-topic.html', context=context_dict)
