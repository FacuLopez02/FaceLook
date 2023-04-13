from django.shortcuts import render
from .models import Post

# Create your views here.

def blog(request):

    lista_posteos = Post.objects.all()
    
    return render(request,'blog/blog.html',{'posteos': lista_posteos})