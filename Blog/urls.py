from django.contrib import admin
from django.urls import include, path
from .views import Articlelistview, Articledetailview, Articlecreateview, Articleupdateview, Articledeleteview

from Blog import views

app_name = "Blog"
urlpatterns = [
    path('', Articlelistview.as_view(), name='Article_list'),
    path('create/', Articlecreateview.as_view(), name='Article_create'),
    path('<int:id>/', Articledetailview.as_view(), name='Article_detail'),
    path('<int:id>/update/', Articleupdateview.as_view(), name='Article_update'),
    path('<int:id>/delete/', Articledeleteview.as_view(), name='Article_delete'),
    path('article/', views.Article_model_view, name='Article_models'),
    path('formart/', views.Article_form_view, name='Article_form'),
    path('raw/', views.Article_raw_view, name='Article_raw'),
    path('art/<int:id>/', views.dynamic_lookup_view, name='Blog_detail'),
    path('<int:id>/delete/', views.log_view, name='log'),
    path('object/', views.object_view, name='object'),
]