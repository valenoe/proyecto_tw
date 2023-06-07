from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.contrib import messages

# Create your views here.


def post_list(request):

    posts = Post.objects.all()
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            messages.success(request, "La publicación fue guardada exitosamente")
        else:
            messages.success(request, "ha ocurrido un error al guardar la publicación")
    post_form = PostForm()
    return render(request, 'blog/post_list.html', {'posts': posts, 'formulario':post_form})
