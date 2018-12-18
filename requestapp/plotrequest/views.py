from django.shortcuts import render
from django.http import HttpResponse

from . import forms

URL_DATA = 'http://127.0.0.1:8000/plots/request/'


def index(request):
    graphform = forms.GraphChoicesForm()
    form = forms.RequestForm()
    ##periodform = forms.PeriodChoicesForm()
    return render(request, 'plotrequest/index.html', {
        'graphform': graphform, 'form': form, 'url_data': URL_DATA})


def options(request):
    kind = request.GET.get('kind')
    choicesform = forms.get_options(kind)
    return render(request, 'plotrequest/options.html', {'choicesform': choicesform})


def date(request):
    period = request.GET.get('period')
    if period == 'custom':
        form = forms.RequestForm()
        return render(request, 'plotrequest/date.html', {'form': form})
    return HttpResponse()
