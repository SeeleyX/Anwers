from django.shortcuts import render

# Create your views here.
def index(request):
	context_dict = {}
	return render(request, 'learn/index.html', context=context_dict)

def astronomy(request):
	context_dict = {}
	return render(request, 'learn/astronomy.html', context=context_dict)