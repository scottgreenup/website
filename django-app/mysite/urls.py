from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('pages.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
]
