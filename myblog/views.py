from django.shortcuts import render


def index(request):
	1/0
    return render(request, 'index.html')
