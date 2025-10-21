from django.contrib.admin import views
from django.urls import path, include

from blog.views import BlogPostCreateView, BlogPostDetailView, HomeView


app_name = "blog"

urlpatterns = [
    path('', HomeView.as_view(), name='home_blog'),
    path('post/<int:pk>/', BlogPostDetailView.as_view(), name='blog_detail'),
    path('form/', BlogPostCreateView.as_view(), name='add_post'),

]