from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from.forms import Rawschoolform
# Create your views here.
from .models import page

def pages_view(request):
     queryset = page.objects.all()

     context = {

        "object_list": queryset,

     }

     return render(request, "school1.html", context)

def dynamic_lookup_view(request, id):
    object = page.objects.all()
    object = page.objects.get(id = id)
    if object == object:
       print(object)
    content = {

        "objects": object.title,
        "objects1": object.section,
        "objects2": object.mode

    }
    return render(request, "school1.html", content)