from django.urls import path
from pages import views

app_name = "pages"
urlpatterns = [
    path('<int:id>/', views.dynamic_lookup_view, name='page_object'),
    path('', views.pages_view, name='pages'),
]