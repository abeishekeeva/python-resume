from django.shortcuts import render


def index(request):
    return render(request, 'index/index.html', {})


def work(request):
	return render(request, 'index/work.html', {})