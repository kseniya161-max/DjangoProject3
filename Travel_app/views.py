from django.shortcuts import render

def home(request):
    """Отображает главную страницу приложения"""
    return render(request, 'home.html')