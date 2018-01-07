from django.shortcuts import render
from django.http import HttpResponse
from .models import Commitment

def index(request):
	context = {
		'response': 'I want to show that I can pass values from controller to view.'
		}

	return render(request, 'app/index.html', context)


def set_commitment(request, user_id, count_frequency, period):
	response = "Your newest commitment of %s commit(s) per %s was created."

	return HttpResponse(response % (count_frequency, period))


def profile(request, user_id):
    # latest_stats = Summary.objects.filter('user_id'=user_id) #search by user_id
    # context = {
    #     'latest_stats': latest_stats,
    # }
    # return render(request, 'app/index.html', context) #passes context to template
    return render(request, 'app/profile.html')

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id) # or get_list_or_404()
#     return render(request, 'polls/detail.html', {'question': question})
