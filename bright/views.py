from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from datetime import datetime


#load homepage
def homepage(request):
    mydata = Post.objects.filter(is_published=True)
    return render(request, 'bright_index.html', {'mycontent': mydata})


#create a new post
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = datetime.now()
            post.save()
            return redirect('/')
        else:
            return render(request, 'bright_post_new.html', {'post_form': form})
    else:
        form = PostForm()
        return render(request, 'bright_post_new.html', {'post_form': form})


#visit page detail page
def post_detail(request, article_id):
    mydata = Post.objects.get(id=article_id)
    return render(request, 'bright_post_detail.html', {'myarticle': mydata})


#delete post
def post_delete(request, article_id):
    mydata = Post.objects.get(id=article_id)
    mydata.delete()
    return redirect('/bright/')

#publish post
def publish_post(request, article_id):
    if request.method == 'POST':
        mydata = Post.objects.get(id=article_id)
        mydata.is_published = True
        mydata.save()
        return redirect('/bright/')
    else:
        return redirect('/bright/')
