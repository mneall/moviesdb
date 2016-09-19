from django.shortcuts import render, redirect

def index(request):
	print "You've reached the index route!"

	return render(request, "app1/index.html")
