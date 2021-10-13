from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import postmode,Comment, CommentUserProfile, PostImage
from .forms import CommentForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,)
from .forms import post_form

# Create your views here.
def homeview(request):
    obj = postmode.objects.all()

    context = {
        "posts": obj
    }
    return render(request, "post_home.html", context)


def aboutview(request):
     context = {

         "title": "About Page"
     }
     return render(request, "post_about.html", context)


#if you want to use a class based view:
#Note class based view use object_list in ListView but we are using posts

class list_view(ListView):
    model = postmode
    template_name = "post_home.html"
    context_object_name = 'posts'
    ordering = ['-date_posted'] # it is use to set the post to the current one
    paginate_by = 4 #It is use to divide the posts in a single page

class Userlist_view(ListView):
    model = postmode
    template_name = "user_post.html"
    context_object_name = 'posts'
    paginate_by = 4

  #we use this to view all the posts of a particular user
    def get_queryset(self):
            user = get_object_or_404(User, username=self.kwargs.get('username'))
            return postmode.objects.order_by('-date_posted').filter(author=user)

class detail_view(DetailView):
    model = postmode
    template_name = "post_detail.html"

    def get_object(self, queryset=None):
        id = self.kwargs.get("id")
        return get_object_or_404(postmode, id=id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #pk = self.kwargs["pk"]
        id = self.kwargs["id"]

        form = CommentForm()
        post = get_object_or_404(postmode, id=id)
        comments = post.comment_set.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form
        return context


    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)

        post = postmode.objects.filter(id=self.kwargs['id'])[0]
        comments = post.comment_set.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form

        if form.is_valid():
            name = request.user.username
            body = form.cleaned_data['comment_body']
            comment = Comment.objects.create(commenter_name=name, comment_body=body, post=post)

        else:
            form = CommentForm()
            context['form'] = form
            return self.render_to_response(context=context)

        return self.render_to_response(context=context)

#We use the loginrequiredmixin so that when the app is logged out
#no user is allowed to create a new post unless the user is logged in
#to avoid null intergrity error

class create_view(LoginRequiredMixin, CreateView):
     form_class = post_form
     template_name = "post_form.html"

     def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

     def get_success_url(self):
         return "/posts/home/"


#Always make sure that the LoginRequiredMixin and UserPassesTestMixin is at the left hand side

class update_view(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = post_form
    template_name = "post_form.html"
    queryset = postmode.objects.all()

    def get_object(self, queryset=None):
        id = self.kwargs.get('id')
        return get_object_or_404(postmode, id=id)

#We use the test_func to ensure that a post is only updated by the user logged in
#and the post he or she did. You cant update another person post except your own. It will return an error

    def test_func(self):
        postmode = self.get_object()
        if self.request.user == postmode.author:
            return True
        else:
            return False

    def get_success_url(self):
        return "/posts/home/"


class delete_view(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = postmode
    template_name = "post_delete.html"

    def get_object(self, queryset=None):
        id = self.kwargs.get("id")
        return get_object_or_404(postmode, id=id)

    def test_func(self):
        postmode = self.get_object()
        if self.request.user == postmode.author:
            return True
        else:
            return False

    def get_success_url(self):
        return "/posts/home/"



def delete_comment(request, pk):
    comment = Comment.objects.filter(object=pk).last()
    object_id = comment.object.id
    comment.delete()
    return redirect(reverse('post-detail', args=[object_id]))


