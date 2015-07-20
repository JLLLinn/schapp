from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from django.shortcuts import render
from django.template import RequestContext, loader

from .models import Question
# Create your views here.
# each view is only responsible for two things
# retuan an Httpresponse or raise exception

#this uses the template
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    #context = RequestContext(request, {
    #    'latest_question_list': latest_question_list,
    #})
    #return HttpResponse(template.render(context))

    #These 2 lines have taken over the former 2 lines
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    #if the question_id doesn't exist, it raises a 404 exception
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question': question})

    #instead of capturing the DoesNotExist exception, which exist at the model layer
    #we use this shortcut "get_object_or_404" that decouple the two layers.
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
