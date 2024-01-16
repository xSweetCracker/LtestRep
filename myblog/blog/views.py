from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostCreateViewForm


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'posts/post.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'
    context_object_name = 'post'


class CreatePostView(CreateView):
    model = Post
    form_class = PostCreateViewForm
    template_name = 'posts/create.html'
    success_url = '/'
