from django.urls import path
from . import views

urlpatterns = [
    path('', views.gethtml_expens, name='gethtml_expens'),
]