from django.shortcuts import render
from .models import expenses

# Create your views here.
def gethtml_expens(request):
    new_exspens =expenses.objects.all()
    return render(request, 'exspenses/exphome.html', {'new_exspens': new_exspens})


