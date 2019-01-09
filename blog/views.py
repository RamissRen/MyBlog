from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
 
 
def home(request):
    return render(request, "partial/home.html")

def single(request, id=None):
    return render(request, "partial/single.html")

urlpatterns = [
    path('',  include('blog.urls')),
    path('admin/', admin.site.urls),
]
 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)