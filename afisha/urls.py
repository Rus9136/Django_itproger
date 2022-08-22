from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    path('', views.get_afisha, name='get_afisha'),
    path('god', views.gods),
    path('gods2', views.gods2),
    re_path(r'about', views.about),
]