from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)
from django.urls import reverse_lazy
from .forms import PostForm
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here


def home(request):
    context = {
        'posts': Post.objects.all(),
        'name': 'Home',
    }
    # pass information to template
    # return an HTTP respons
    return render(request, 'posts/home.html', context)


class ListPostView(ListView):
    model = Post
    template_name = 'posts/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2


class DetailPostView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin, CreateView ):
    
    model = Post
    fields = ['title', 'cover', 'caption','date_posted']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'caption']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
