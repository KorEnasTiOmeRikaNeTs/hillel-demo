from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.shortcuts import render, redirect
from .models import Post


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


class PostUpdate(LoginRequiredMixin, UpdateView):
	model = Post
	template_name = 'post_update.html'
	fields = ('title', 'text',)


def create_user(request):
    form = UserCreationForm(request.POST or None)
    if form.is_bound and form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'register.html', {'form': form})


