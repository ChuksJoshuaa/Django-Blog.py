from django.shortcuts import render

# Create your views here.

from .forms import gameform
from .models import game
from .forms import Rawgameform

def game_view(request):
    my_form = Rawgameform()
    if request.method == "POST":
       my_form = Rawgameform(request.POST)
       print(my_form)
       if my_form.is_valid():
          print(my_form.cleaned_data)

       else:
          print(my_form.errors)
    content = {

        "form" : my_form,
    }
    return render(request, "room.html", content)






#def game_view(request):
    #print(request.GET)
    #print(request.POST)
    #if request.method == "POST":
        #print(request.POST)
    #else:
        #my_new_title = request.POST.get("title")
        #print(my_new_title)
    #content = {}
    #return render(request, "room.html", content)




#def game_view(request):
    #form = gameform(request.POST or None)
    #if form.is_valid():
    # form.save()
    #form = gameform()
    #form = gameform()
    #content = {
       # "form": form
    #}
   # return render(request, "room.html", content)