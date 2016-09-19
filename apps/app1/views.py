from django.shortcuts import render, redirect
from .models import Movies, Actors

def index(request):
	# print "You've reached the index route!"
	movies = Movies.objects.all()
	print movies
	context = {'movies':movies}
	return render(request, "app1/index.html",context)

def movietitle(request):
	Movies.objects.create(title=request.POST['title'], movies=request.POST['movies'])
	return redirect('/')
