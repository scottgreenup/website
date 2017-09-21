from django.http import HttpResponse
from django.views import View


class PostsView(View):
    def get(self, request):
        return HttpResponse("Hi")


class PostView(View):
    def get(self, request, title):
        return HttpResponse("title: {}".format(title))
