from blog import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.PostsView.as_view(), name='posts'),
    url(r'^(?P<title>[A-Za-z0-9-_]+)/$', views.PostView.as_view(), name='post')
]
