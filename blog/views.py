from django.template.defaultfilters import default
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import BlogPost


class HomeView(ListView):
    """Представление главной страницы"""
    model = BlogPost
    template_name = 'home_blog.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)


class BlogPostDetailView(DetailView):
    """ Отображает записи каждого отдельного блога"""
    model = BlogPost
    template_name = 'detail_blog.html'
    context_object_name = 'post' # В шаблоне ссылаемся на него

    def get_object(self, queryset = None):
        post = super().get_object(queryset)
        post.views_count += 1
        post.save()
        return post


class BlogPostCreateView(CreateView):
    """Создает запись Блога"""
    model = BlogPost
    template_name = 'form_blog.html'
    fields = ['header', 'content', 'preview','is_published']
    success_url = reverse_lazy('blog:home_blog')


class BlogUpdateView(UpdateView):
    """Редактирует запись Блога"""
    model = BlogPost
    template_name = 'form_blog.html'
    fields = ['header', 'content', 'preview', 'is_published']


    def get_success_url(self):
        return reverse_lazy('blog:blog_detail', kwargs={'pk': self.object.pk})


class BlogDeleteView(DeleteView):
    """Удаляет запись Блога"""
    model = BlogPost
    template_name = 'blog_confirm_delete.html'
    success_url = reverse_lazy('blog:home_blog')


