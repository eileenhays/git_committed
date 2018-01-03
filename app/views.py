from django.shortcuts import render
from django.http import HttpResponse
from .models import UserProfile, Commitment

def index(request):
	context = {'response': 'I want to show that I can pass values from controller to view.'}
	
	return render(request, 'app/index.html', context)


def set_commitment(request, user_id, count_frequency, period):
	response = "Your newest commitment of %s commit(s) per %s was created."

	return HttpResponse(response % (count_frequency, period))


def progress(request, user_id):
	response = "Progress was made"

	return HttpResponse(response)