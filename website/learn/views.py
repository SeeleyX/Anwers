from django.shortcuts import render, redirect
from django.urls import reverse
from learn.forms import LearnerUserForm 
from django.contrib.auth import authenticate, login, logout

def index(request):
	context_dict = {}
	return render(request, 'learn/index.html', context=context_dict)

def astronomy(request):
	context_dict = {}
	return render(request, 'learn/astronomy.html', context=context_dict)

def user_login(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")

		user = authenticate(username = username, password = password)

		if user:
			if user.is_active:
				login(request, user)
				return redirect(reverse("learn:learn_base"))
			else:
				return HttpResponse("Account disabled")
		else:
			print(f"Invalid login details supplied: {username}, {password}")
			return HttpResponse("Invalid login details supplied")
	else:
		learner_user_form = LearnerUserForm()
		return render(request, 'learn/login.html', context={'learner_user_form' : learner_user_form})
	return response

def user_register(request):
	registered = False

	if request.method == "POST":
		learner_user_form = LearnerUserForm(request.POST)

		if learner_user_form.is_valid():
			learner_user = learner_user_form.save()
			learner_user.set_password(learner_user.password)
			learner_user.save()

			registered = True
			login(request, learner_user)
		else:
			print(student_user_form.errors, student_user_profile_form.errors)
	else:
		learner_user_form = LearnerUserForm()
	return render(request, 'learn/register.html', context={'learner_user_form' : learner_user_form, 'registered' : registered})


def learn_base(request):
	return redirect("/")