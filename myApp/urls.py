"""myApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
#from pages import views
from users import views
#from game import views


#from school import views

urlpatterns = [
     path('admin/', admin.site.urls),
     path('register/', views.user_registerview, name='user_register'),
     path('login/', auth_views.LoginView.as_view(template_name='user_login.html'), name='user_login'),
     path('logout/', auth_views.LogoutView.as_view(template_name='user_logout.html'), name='user_logout'),
     path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
          name='password_reset'),
     path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
          name='password_reset_done'),
     path('password-reset-confirm/<uidb64>/<token>/',
          auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
          name='password_reset_confirm'),
     path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
          name='password_reset_complete'),
     path('profile/', views.profile, name='user_profile'),
     path('Blog/', include('Blog.urls')),
     path('sapa/', include('sapa.urls')),
     path('posts/', include('posts.urls')),
     path('product/', include('product.urls')),
     #path('pages/', include('pages.urls')),
    #path('product/<int:id>/delete/', views.product_detail_view, name='product_delete'),
    #path('create', views.product_create_view, name='create'),


]

if settings.DEBUG:
         urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
