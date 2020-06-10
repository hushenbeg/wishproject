# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import datetime

# Create your views here.

def greetings_info(request):

    date = datetime.datetime.now()
    hours = datetime.datetime.now().strftime('%H')

    msg = 'Hello Guest very Good '

    if hours < 12 :
        msg = msg + " MORNING"
    
    elif hours < 16:
        msg = msg + " AFTERNOON"
    
    elif hours < 21:
        msg = msg + " EVENING"
    
    else:
        msg = msg+ " NIGHT"
    
    return render(request, 'displayapp/result.html', {'msg':msg,'date':date})


