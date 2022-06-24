from django.shortcuts import render, redirect
from django.urls import reverse
from learn.forms import LearnerUserForm 

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
				return redirect(reverse("learn:index"))
			else:
				return HttpResponse("Account disabled")
		else:
			print(f"Invalid login details supplied: {username}, {password}")
			return HttpResponse("Invalid login details supplied")
	else:
		learner_user_form = LearnerUserForm()
		return render(request, 'learn/login.html', context={'learner_user_form' : learner_user_form})
	return response

def learn_base(request):
	return redirect("/")