from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .models import Post


class PublicPostList(ListView):
    model = Post
    template_name = 'Public.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['posts'] = Post.objects.order_by('-created_at')
        return context


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
    pk_url_kwarg = 'pk'

    def get_object(self, **kwargs):
        post = super().get_object(**kwargs)
        if not post.created_by == self.request.user:
            raise PermissionDenied
        return post


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('home')

    def get_object(self, **kwargs):
        post = super().get_object(**kwargs)
        if not post.created_by == self.request.user:
            raise PermissionDenied
        return post

    def get_success_url(self):
        return self.success_url


def create_user(request):
    form = UserCreationForm(request.POST or None)
    if form.is_bound and form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'register.html', {'form': form})
