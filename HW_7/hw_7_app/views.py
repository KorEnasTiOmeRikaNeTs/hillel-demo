from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseNotFound
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.shortcuts import render, redirect
from .models import Post


class PublicPostList(ListView):
    model = Post
    template_name = 'Public.html'


class PostList(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'post_list.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = ('title', 'text',)

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ('title', 'text',)
    pk_url_kwarg = 'id'

    def get_object(self, **kwargs):
        post = super().get_object(self, **kwargs)
        if not post.created_by == self.request.user:
            raise PermissionDenied
        return post


def create_user(request):
    form = UserCreationForm(request.POST or None)
    if form.is_bound and form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'register.html', {'form': form})
