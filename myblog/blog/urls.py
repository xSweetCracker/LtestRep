from django.urls import path
from .views import PostListView, PostDetailView, CreatePostView

app_name = 'post'

urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('blog/<slug:slug>/', PostDetailView.as_view(), name='detail'),
    path('posts/create/', CreatePostView.as_view(), name='create')
]
