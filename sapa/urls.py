from django.urls import path



from sapa import views
app_name = "sapa"
urlpatterns = [
   path("list/", views.listview.as_view(), name="sapa_list"),
   path("<int:id>/detail/", views.detailview.as_view(), name="sapa_detail"),
   path("create/", views.createview.as_view(), name="sapa_create")


]