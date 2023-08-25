from django.shortcuts import get_object_or_404, redirect, render
from .models import Post


def PostsViews(request):
    context ={}
 
    # add the dictionary during initialization
    posts = Post.objects.all()
    context ={
        'posts':posts,
        'page_title':'blog',
    }
    return render(request, 'pages/posts/index.html', context)



def PostDetailView(request, id):
    context ={}
 
    # add the dictionary during initialization
    context["data"] = Post.objects.get(id = id)
         
    return render(request, "pages/posts/post_detail_view.html", context)