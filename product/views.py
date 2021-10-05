from django.shortcuts import render, get_object_or_404, redirect, reverse
from .forms import productform
from .models import product
from django.views import View
from django.views.generic import CreateView, UpdateView

# Create your views here.


def dynamic_lookup_view(request, id):
    obj = product.objects.get(id= id)

    context = {

        "form1": obj.name,
        "form2": obj.Description,
        "form3": obj.Prices,
        "form4": obj.Summary,

    }
    return render(request, "product/product_look.html", context)



def productobjectview(request):
     formmy = productform()
     formmy = productform(request.POST)
     if request.method == "POST":
         print(formmy)
         try:
            if formmy.is_valid():
                print(formmy.cleaned_data)

         except ValueError:
                print("This is an error")


     context = {

       "form1": formmy

     }
     return render(request, "product/product_object.html", context)


def productdetailview(request):
    queryset = product.objects.all()

    context = {

        "object_list": queryset

    }
    return render(request, "product/product_detail.html", context)

class Courseview(View):
      template_name = "product/product_home.html"
      def get(self, request, *args, **kwargs):
          return render(request, self.template_name, {})


class Coursedetailview(View):
     template_name = "product/product_detail.html"

     def get(self, request, id=None, *args, **kwargs):

         queryset = product.objects.all()
         context = {
            "object_list": queryset
         }
         return render(request, self.template_name, context)


class createview(CreateView):
     template_name = "product/product_look.html"
     form_class = productform
     queryset = product.objects.all()

     def get_success_url(self):
         return reverse("product:product_detail")


class detailview(View):
    template_name = "product/product_lay.html"
    def get(self, request, id, *args, **kwargs):

        obj = product.objects.get(id=id)

        context = {
            "object": obj.name,
            "object1": obj.Description,
            "object2": obj.Prices,
            "object3": obj.Summary
        }
        return render(request, self.template_name, context)


class updateview(UpdateView):
    template_name = "product/product_object.html"
    queryset = product.objects.all()
    form_class = productform

    def get_object(self, queryset=None):
        id = self.kwargs.get("id")
        return get_object_or_404(product, id=id)




