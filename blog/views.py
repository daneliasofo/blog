from django.shortcuts import render

from .models import Post

def post_list(request):
    posts = Post.objects.select_related(
        'author',        
        'author__profile'  
    )

    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    (
        Post.objects.prefetch_related(
            'comments__user',  
            'tags'            
        ),
        id=post_id
    )

    return render(request, 'blog/post_detail.html', {'post': post})