from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from datetime import datetime


def homepage(request):
    mydata = Post.objects.all()
    return render(request, 'Nathaniel_index.html', {'mycontent': mydata})


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = datetime.now()
            post.save()
            return redirect('/Nathaniel/')
        else:
            return render(request, 'Nathaniel_post_new.html', {'post_form': form})
    else:
        form = PostForm()
        return render(request, 'Nathaniel_post_new.html', {'post_form': form})


def post_detail(request, article_id):
    mydata = Post.objects.get(id=article_id)
    return render(request, 'Nathaniel_post_detail.html', {'myarticle': mydata})
