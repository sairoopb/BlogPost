from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_list.html', {'form': form})