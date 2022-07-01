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
		'index': 'phys',

		'sub_topics': [
		{
        'title': 'Thermal Physics',
        'image': 'Thermal',
        'url': 'thermal_physics',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
      	},
      	{
        'title': 'Newtonian Dynamics',
        'image': 'Newtonian',
        'url': 'newtonian_dynamics',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
     	},
      	{
        'title': 'Oscillating Systems',
        'image': 'Oscillating_Systems',
        'url': 'oscillating_systems',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
      	},
      	{
        'title': 'Electricity and Magnetism',
        'image': 'Electricity',
        'url': 'electricity_magnetism',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
      	},
      	{
        'title': 'Physics of Solids',
        'image': 'POS',
        'url': 'physics_of_solids',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
      	},
      	{
        'title': 'Nuclear and Particle Physics',
        'image': 'NPP',
        'url': 'nuclear_particle_physics',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
     	},
      	{
        'title': 'Optics',
        'image': 'Optics',
        'url': 'optics',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
      	},
      	{
        'title': 'Quantum and Classical Waves',
        'image': 'Quantum_Waves',
        'url': 'quantum_classical_waves',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
      	}]
	}
	return render(request, 'learn/topic.html', context=context_dict)


def maths(request):
	context_dict = {

		'topic_title': 'Maths',
		'index': 'maths',

		'sub_topics': [
		{
        'title': 'Linear Algebra',
        'image': 'Linear_Algebra',
        'url': 'linear_algebra',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
      	},
      	{
        'title': 'Abstract Algebra and Groups',
        'image': 'Abstract_Algebra',
        'url': 'abstract_algebra_groups',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
     	},
      	{
        'title': 'Real Analysis',
        'image': 'Real_Analysis',
        'url': 'real_analysis',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
      	},
      	{
        'title': 'Multivariable Calculus',
        'image': 'Multivariable_Calculus',
        'url': 'multivariable_calculus',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
      	},
      	{
        'title': 'Mechanics',
        'image': 'Mechanics',
        'url': 'mechanics',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
      	},
      	{
        'title': 'Mathimatical Methods & Modelling',
        'image': 'Mathematical_Models',
        'url': 'mathematical_modelling',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
     	}]
	}
	return render(request, 'learn/topic.html', context=context_dict)


def computerScience(request):
	context_dict = {

		'topic_title': 'Computer Science',
		'index': 'comp',

		'sub_topics': [
		{
        'title': 'Text as Data',
        'image': 'Linear_Algebra',
        'url': 'text_as_data',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
      	},
      	{
        'title': 'Programming Languages',
        'image': 'Programming_Languages',
        'url': 'programming_languages',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
     	},
      	{
        'title': 'Data-Fundementals',
        'image': 'Real_Analysis',
        'url': 'data_fundementals',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
      	},
      	{
        'title': 'Algorithmics',
        'image': 'Multivariable_Calculus',
        'url': 'algorithmics',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
      	}]
	}
	return render(request, 'learn/topic.html', context=context_dict)



def learn_base(request):
	return redirect("/")


def maths_linear_algebra(request):
	context_dict = {
		'sub_topic_title': 'Linear Algebra',
		'href': 'linear_algebra',

		'sub_sub_topics': [
		{
        'title': 'The Determinant',
        'image': '',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
      	},
      	{
        'title': 'The Determinant',
        'image': '',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
     	},
      	{
        'title': 'The Determinant',
        'image': '',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
      	},
      	{
        'title': 'The Determinant',
        'image': '',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
      	},
      	{
        'title': 'The Determinant',
        'image': '',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
      	},
      	{
        'title': 'The Determinant',
        'image': '',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit, nobis at. Ipsa vel ut assumenda modi culpa. Optio accusantium, vel praesentium voluptatum explicabo pariatur officia modi quas earum consectetur dolar . Lorem ipsum dolor, sit amet consectetur adipisicing elit. Amet voluptatum impedit fugit sit, corrupti rem, quam iusto, excepturi velit exercitationem atque consequuntur consectetur eum nam facilis? Minima asperiores quibusdam nemo!',
     	}]
	}
	return render(request, 'learn/sub-topic.html', context=context_dict)
