from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import BlogPost


class HomeView(ListView):
    """Представление главной страницы"""
    model = BlogPost
    template_name = 'home_blog.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return BlogPost.objects.all()


class BlogPostDetailView(DetailView):
    """ Отображает записи каждого отдельного блога"""
    model = BlogPost
    template_name = 'detail_blog.html'
    context_object_name = 'post' # В шаблоне ссылаемся на него


class BlogPostCreateView(CreateView):
    """Создает запись Блога"""
    model = BlogPost
    template_name = 'form_blog.html'
    fields = ['header', 'content', 'preview','is_published']
    success_url = reverse_lazy('blog:post_list')


class BlogUpdateView(UpdateView):
    """Редактирует запись Блога"""
    model = BlogPost
    template_name = 'form_blog.html'
    fields = ['header', 'content', 'preview', 'is_published']
    success_url = reverse_lazy('blog:post_list')


class BlogDeleteView(DeleteView):
    """Удаляет запись Блога"""
    model = BlogPost
    template_name = 'blog_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')


