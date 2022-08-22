from django.shortcuts import render
from django.http import HttpResponse
from .models import afisha_model

def get_afisha(request):
    item = afisha_model.objects.all()

    #item = ({'title': 'as', 'date': 'asd'})


    return render(request, 'afisha/tour.html', {'item': item})
    #return render(request, 'main/about.html')



def gods(request):
    return HttpResponse("<h2>gods </h2>")



def gods2(request):
    return HttpResponse("<h2>gods 2 ss</h2>")


def about(request):
    return HttpResponse("<h2>about страница</h2>")