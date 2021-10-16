from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets
from .models import Blogger
from .serializer import BloggerSerializer

class BloggerViewSet(viewsets.ModelViewSet):
    queryset = Blogger.objects.all()
    serializer_class = BloggerSerializer
    
    # def update(self, request, *args, **kwargs):
    #     return super().update(request, *args, **kwargs)


@csrf_exempt
def data_end(request):
    if request.method == 'POST':
        body = request.body
        print("=====================")
        print(body)
    return HttpResponse(status=200) 
    
