from django.shortcuts import render

from AppCoder.models import Familiar


# Create your views here.

def index(request):

    familiares = Familiar.objects.all()
    
    ctx = {'familiares': familiares}

    return render(request, 'AppCoder/index.html', ctx)