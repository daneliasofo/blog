from django.views.generic import ListView,DetailView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"
    object_name = "post"

    def get_queryset(self):
        return (
            Post.objects
            .select_related("author", "author__profile")
            .all()
        )


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    object_name = "post"

    def get_queryset(self):
        return (
            Post.objects
            .select_related("author")
            .prefetch_related(
                "comments__author",
                "tags"
            )
            .all()
        )
