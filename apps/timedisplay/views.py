from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
import datetime

def index(request):
#   context = {
#   "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
#   }
    context = {
    "time": datetime.datetime.now()
    }
    return render(request,'timedisplay/time.html', context)