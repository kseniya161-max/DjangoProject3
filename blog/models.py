from django.db import models

class BlogPost(models.Model):
    header = models.CharField(max_length = 200 )
    content = models.TextField()
    preview = models.ImageField(upload_to='blog_previews/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    views_count = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'


    def __str__(self):
        return f'{self.header}-{self.views_count}'
