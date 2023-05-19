from django.shortcuts import render
from .models import Post, Categoria

# Create your views here.

def blog(request):

    lista_posteos = Post.objects.all()
    lista_categorias = Post.objects.all().distinct("categorias")

    return render(request,'blog/blog.html',{'posteos': lista_posteos,'posteos_no_rep': lista_categorias})

def categoria(request, categoria_id):
    
    categoria = Categoria.objects.get(id=categoria_id)
    
    lista_posteos = Post.objects.filter(categorias=categoria)
    lista_categorias = Post.objects.filter(categorias=categoria).distinct("categorias")
    
    return render(request, 'blog/categoria.html',{'categoria':categoria, 'posteos': lista_posteos, 'posteos_no_rep': lista_categorias})