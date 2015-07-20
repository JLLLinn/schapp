from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from django.shortcuts import render
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse

from .models import Choice, Question


# Create your views here.
# each view is only responsible for two things
# return an HttpResponse or raise exception

# this uses the template
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = RequestContext(request, {
    #    'latest_question_list': latest_question_list,
    # })
    # return HttpResponse(template.render(context))

    # These 2 lines have taken over the former 2 lines
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # if the question_id doesn't exist, it raises a 404 exception
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question': question})

    # instead of capturing the DoesNotExist exception, which exist at the model layer
    # we use this shortcut "get_object_or_404" that decouple the two layers.
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


# This handles the vote form's post stuff
# Request is a HttpRequest obj, refer to tutorial 3
def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    # handles KeyError that is raised when the post data doesn't exist
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
