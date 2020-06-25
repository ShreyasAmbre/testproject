from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'name': 'Shreyas'})


def add(request):
    n1 = int(request.POST["num1"])
    n2 = int(request.POST["num2"])
    res = n1 + n2
    print(res)

    return render(request, 'result.html', {'Result': res})
