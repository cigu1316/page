from django.shortcuts import render
from appblog.models import Post 
from appblog.models import Categorias



def blog(request):
    post=Post.objects.all()
    return render(request,'blog/blog.html',{'post':post})

def categoria(request,categoria_id):
    categoria=Categorias.objects.get(id=categoria_id)
    post = Post.objects.filter(categorias=categoria_id)
    return render(request,'blog/categoria.html',{'categorias':categoria,'post':post})

   