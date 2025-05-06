from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView

from .models import Type


class CreateType(CreateView):
    model = Type
    fields = ['name']
    template_name = 'type_form.html'


class DirecotryView(FormView):
    model = Type
    
    template_name = 'index.html'
