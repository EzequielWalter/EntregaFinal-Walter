from unittest import loader
from django.http import HttpResponse


from django.http import HttpResponse
from datetime import datetime, timedelta
from django.template import Context, Template, loader
from django.shortcuts import render, redirect
import random
from home.forms import BusquedaFamiliarFormulario, FamiliarFormulario

from home.models import Familiar


def about(request):
    
    return render(request, 'home/about.html')

def index(request):
    
    return render(request, 'home/index.html')