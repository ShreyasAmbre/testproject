from django.shortcuts import render
from .models import Destination


# Create your views here.
def index(request):
    des = Destination.objects.all()
    return render(request, 'index.html', {'dests': des})
