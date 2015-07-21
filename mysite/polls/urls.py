from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    # url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    # the name of url here is for reference back to the url in template
    # find the back reference in polls/index.html
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    # now we amend it to suit our needs
    # note that here it is a generic view that we are using
    #   as refer back to the views file
    #   also we are using pk instead of question_id instead
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
