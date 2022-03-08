from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post
    template_name = 'news_list.html'
    context_object_name = 'news'


class PostDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'
