# Create your views here.
from django.http import HttpResponse
from polls.models import Poll
from django.template import Context, loader
from django.shortcuts import render
from django.utils.translation import ugettext as _

def index(request):
    print "language code : " + request.LANGUAGE_CODE
    output = _("Welcome to my site. ")
    output += "<br>The language code used is " + request.LANGUAGE_CODE
    return HttpResponse(output)

'''
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)
'''

def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)
