from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.template import RequestContext

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    pposts = {
        'Title':posts
    }
    return render(request, 'blog/post_list.html', context=pposts)
    

