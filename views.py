from django.shortcuts import render
from django.views.generic import TemplateView

def pattern_def(request):
    return render(request, 'pattern_def.html')


