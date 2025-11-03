from django.contrib.admin import views
from django.urls import path, include

from blog.views import BlogPostCreateView, BlogPostDetailView, HomeView, BlogUpdateView,BlogDeleteView


app_name = "blog"

urlpatterns = [
    path('', HomeView.as_view(), name='home_blog'),
    path('post/<int:pk>/', BlogPostDetailView.as_view(), name='blog_detail'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_update'),
    path('form/', BlogPostCreateView.as_view(), name='add_post'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
]