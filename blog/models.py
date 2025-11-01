from django.db import models
from django.conf import settings

class BlogPost(models.Model):
    header = models.CharField(max_length = 200 )
    content = models.TextField()
    preview = models.ImageField(upload_to='blog_previews/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    views_count = models.PositiveIntegerField(default=0)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец поста')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        permissions = [
            ('can_publish_blog_post', 'Can publish blog post'),
            ('can_unpublish_blog_post', 'Can unpublish blog post'),
            ('can_delete_blog_post', 'Can delete blog post'),
        ]


    def __str__(self):
        return f'{self.header}-{self.views_count}'
