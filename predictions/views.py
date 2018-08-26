from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from .forms import NewPredictionForm
from django.http import HttpResponse
from . import predict
# Create your views here.


class PredictionsView(TemplateView):
    template_name = 'predictions/view-all.html'


class PredictionsAdd(TemplateView):
    template_name = 'predictions/add.html'

    def get_context_data(self, **kwargs):
        context = super(PredictionsAdd, self).get_context_data(**kwargs)
        form = NewPredictionForm()
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        file = request.FILES['myfile']
        pre = predict.pre_process(file)
        graph = predict.plot_graph(pre)
        return HttpResponse('processing...')
