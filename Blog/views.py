from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.

from .models import Article
from .forms import Articleform
from .forms import RawArticleform

def Article_model_view(request):
    obj = Article.objects.get(id=1)
    objj = Article.objects.all()
    model = Article

    content = {
        "object": objj,
        "the_title": obj.title,
        "the_detail": obj.details,
        "the_item": obj.items,
        "the_price": obj.price
    }
    return render(request, "article_list.html", content)

def Article_form_view(request):
        my_form = Articleform()
        my_form = Articleform(request.POST or None)
        if request.method == "POST":
            print(my_form)
            if my_form.is_valid():
                my_form.save()

            else:
                return my_form

        content = {

           "form": my_form

        }
        return render(request, "article_detail.html", content)


def Article_raw_view(request, *args, **kwargs):
    my_formm = RawArticleform()
    my_formm = RawArticleform(request.POST)
    if request.method == "POST":
        print(my_formm)
        try:
            if my_formm.is_valid():
               print(my_formm.cleaned_data)

        except ValueError:
              print(" This is error!! ")

    content = {

        "form1": my_formm

    }
    return render(request, "article_detail.html", content)

def dynamic_lookup_view(request, id):
    login = Article.objects.get(id= id)

    content = {

        "login1": login.details,
        "login2": login.items,
        "login3": login.price

    }
    return render(request, "article_list.html", content)

def log_view(request, id):
    log1 = get_object_or_404(Article, id=id)
    try:
        if request.method == "POST":
            log1.delete()
            return redirect("/Blog/raw/")
    except ValueError:
         return "This is an error"

    content = {
        "log1": log1
    }

    return render(request, "article_object.html", content)

def object_view(request):
    queryset = Article.objects.all()

    content = {
        "object_list": queryset
    }
    return render(request, "article_list.html", content)


class Articlelistview(ListView):
    template_name = "article_detail.html"
    queryset = Article.objects.all()

class Articledetailview(DetailView):
    template_name = "article_object.html"
    queryset = Article.objects.all()

    def get_object(self, queryset=None):
        id = self.kwargs.get("id")
        return get_object_or_404(Article, id=id)

#The create view is very similar to the update view
class Articlecreateview(CreateView):
    template_name = "article_create.html"
    form_class = Articleform
    queryset = Article.objects.all()

    # we use the below form_valid to get the date in the terminal just like the cleaned_data style
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # to override the redirect url, we use
    #def get_success_url(self):
        #return "/Blog/formart"
# to update or edit a particular view, we use the update view

class Articleupdateview(UpdateView):
    template_name = "article_create.html"
    form_class = Articleform
    queryset = Article.objects.all()

    def get_object(self, queryset=None):
        id = self.kwargs.get("id")
        return get_object_or_404(Article, id=id)

# the delete view is the same as the detail view

class Articledeleteview(DeleteView):
    template_name = "article_object.html"
    queryset = Article.objects.all()

    def get_object(self, queryset=None):
        id = self.kwargs.get("id")
        return get_object_or_404(Article, id=id)

    def get_success_url(self):
        return "/Blog/create/"

#A user authentication system used for corey website, this
#is the solution you found yourself.

#from django.shortcuts import render, redirect, reverse
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth import login, authenticate
#from django import forms
#from .models import Profile
#from django.contrib.auth.decorators import login_required
#from django.contrib import messages




#def registerview(request):
 #   form1 = Rawuserform()
        #   if request.method == "POST":
        #  form1 = Rawuserform(request.POST)
        #if form1.is_valid():
        #   print(form1.cleaned_data)
        #  Username = form1.cleaned_data.get('Username')
        #  Password = form1.cleaned_data.get('Password')
        # Re_Password = form1.cleaned_data.get('Re_Password')
        # if Password != Re_Password:
        #    raise forms.ValidationError("Password does not match")
        #elif len(Password) < 8:
        #  raise forms.ValidationError("Password too short!!")
        #else:
        # user = authenticate(username=Username, password=Password, re_password=Re_Password)
        # login(request, user)
    # return redirect("post-home")

        #else:
        #form1 = Rawuserform()
    #context = {
    # "form": form1
    #}
# return render(request, "user_register.html", context)