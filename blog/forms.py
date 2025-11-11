from django.forms import ModelForm, forms

from blog.models import BlogPost


class BlogPostForm(ModelForm):
    """Настраиваем форму для создания поста"""
    class Meta:
        model = BlogPost
        fields = ['header', 'content', 'preview', 'is_published']
        widgets = {
            'content': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Введите содержание поста', 'rows': 10}),
        }