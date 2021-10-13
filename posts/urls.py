from django.urls import path
from posts import views


urlpatterns = [
    #path("home/", views.homeview, name='post-home'),
    path('home/', views.list_view.as_view(), name='post-home'),
    path('user/<str:username>', views.Userlist_view.as_view(), name='user-post'),
    path('<int:id>/detail/', views.detail_view.as_view(), name='post-detail'),
    path('<int:id>/update/', views.update_view.as_view(), name='post-update'),
    path('<int:id>/delete/', views.delete_view.as_view(), name='post-delete'),
    path('<int:id>/delete-comment/', views.delete_comment, name='delete-comment'),
    path('create/', views.create_view.as_view(), name='post-create'),
    path('about/', views.aboutview, name='post-about')

]

