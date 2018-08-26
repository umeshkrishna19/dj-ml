from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.


def test(request):
    return HttpResponse('test')


class PredictionsHomePage(TemplateView):
    template_name = 'test.html'
