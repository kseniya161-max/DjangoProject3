from django.core.exceptions import PermissionDenied
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

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    """Редактирует запись Блога"""
    model = BlogPost
    template_name = 'form_blog.html'
    fields = ['header', 'content', 'preview', 'is_published']
    success_url = reverse_lazy('blog:home_blog')


    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.owner != request.user and not request.user.has_perm('blog.can_publish_blog_post') and not request.user.has_perm('blog.can_unpublish_blog_post'):
            raise PermissionDenied (" У вас нет прав")
        return super().dispatch(request, *args, **kwargs)


class BlogDeleteView(DeleteView):
    """Удаляет запись Блога"""
    model = BlogPost
    template_name = 'blog_confirm_delete.html'
    success_url = reverse_lazy('blog:home_blog')


    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.owner != request.user and not request.user.has_perm('blog.can_delete_blog_post'):
            raise PermissionDenied(" У вас нет прав на удаление поста")
        if not request.user.has_perm('blog.can_delete_blog_post'):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


