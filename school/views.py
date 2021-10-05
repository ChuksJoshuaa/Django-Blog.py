from django.shortcuts import render

# Create your views here.

from .forms import schoolform
from .forms import Rawschoolform
from .models import school

def dynamic_lookup_view(request, id):
     obj = school.objects.all()
     obj = school.objects.get(id= id)
     context = {
         "object": obj,
     }
     return render(request, "school_log.html", context)

#def school_view(request, *args, **kwargs):
    #form = schoolform(request.POST or None)
    #if form.is_valid():
        #form.save()
    #context = {
       # "form": form
    #}
    #return render(request, "school_log.html", context)
