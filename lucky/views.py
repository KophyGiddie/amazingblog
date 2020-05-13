from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from datetime import datetime

def index(request):
    posts = Post.objects.all()
    return render(request, 'lucky_index.html', {'mycontent': posts})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = datetime.now()
            post.save()
            return redirect('/lucky/')
        else:
            return render(request, 'lucky_post_new.html', {'post_form': form})
    else:
        form = PostForm()
        return render(request, 'lucky_post_new.html', {'post_form': form})
    
def post_detail(request, article_id):
    post = Post.objects.get(id=article_id)
    return render(request, 'lucky_post_detail.html', {'myarticle': post})