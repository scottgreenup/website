from blog.models import Post
from django.shortcuts import render
from django.views import View


class PostsView(View):
    def get(self, request):
        try:
            posts = Post.objects.all().order_by("-created_at")
        except:
            posts = None

        context = {'posts': posts}
        return render(request, 'blog/posts.html', context)


class PostView(View):
    def get(self, request, title):
        try:
            post = Post.objects.get(title=title)
        except Post.DoesNotExist:
            post = None

        context = {'post': post}
        return render(request, 'blog/post.html', context)
