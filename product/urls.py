from django.contrib import admin
from django.urls import include, path


from product import views

app_name = "product"
urlpatterns = [
    path('home/', views.Courseview.as_view(), name='product_home'),
    path('detail/', views.Coursedetailview.as_view(), name='product_detail'),
    path('<int:id>/update/', views.updateview.as_view(), name='product_update'),
    path('raw/', views.createview.as_view(), name='product_raw'),
    path('<int:id>/lay/', views.detailview.as_view(), name='product_lay'),
   # path('<int:id>/create/', views.dynamic_lookup_view, name='product_create'),
    path('detail/', views.productdetailview, name='product_detail')

]