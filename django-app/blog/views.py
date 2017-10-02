from blog.models import Post
from django.shortcuts import render
from django.views import View
from markdown2 import markdown


def render_post(post):

    content = markdown(post.content, extras=[
        "fenced-code-blocks",
    ])

    return {
        'title': post.title,
        'created_at': post.created_at.strftime("%B {}, %Y".format(
            post.created_at.day)),
        'content': content,
        'author': post.author
    }


class PostsView(View):
    def get(self, request):
        try:
            posts = Post.objects.all().order_by("-created_at")
        except:
            posts = None

        modified = []

        for post in posts:
            modified.append(render_post(post))

        context = {'posts': modified}
        return render(request, 'blog/posts.html', context)


class PostView(View):
    def get(self, request, title):
        try:
            post = Post.objects.get(title=title)
        except Post.DoesNotExist:
            post = None

        if post:
            post = render_post(post)
        context = {'post': post}
        return render(request, 'blog/post.html', context)
