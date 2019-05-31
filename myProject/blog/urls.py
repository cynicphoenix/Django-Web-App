from django.conf.urls import url
from django.urls import path
from . import views
from .views import (
    PostListView, 
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)

urlpatterns = [
    path('about/', views.about, name='blog-about'),
    path('obliviate/', views.obliviate, name='blog-obliviate'),
    path('post/<int:pk>/', PostDetailView.as_view() , name='post-detail'),
    path('post/new/', PostCreateView.as_view() , name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('', PostListView.as_view() , name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view() , name='user-posts'),
] 