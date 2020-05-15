from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from datetime import datetime


#load homepage and list of post that were published
def homepage(request):
    mydata = Post.objects.filter(is_published=True)
    return render(request, 'bright_index.html', {'mycontent': mydata})

#lis of post that were not published
def unpublished_posts(request):
    mydata = Post.objects.filter(is_published=False)
    return render(request, 'bright_index.html', {'mycontent': mydata})

#create a new post
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
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

#edit a post
def edit_post(request, article_id):
    my_post = Post.objects.get(id=article_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=my_post)
        if form.is_valid():
            post = form.save(commit=False)
            post.modified_date = datetime.now()
            post.save()
            return redirect('/bright/')
        else:
            return render(request, 'bright_post_edit.html', {'post_form': form})
    else:
        form = PostForm(instance=my_post)
        return render(request, 'bright_post_edit.html', {'post_form': form, 'article_id': article_id})


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

#unpublish a particular post
def unpublish_post(request, article_id):
    if request.method == 'POST':
        mydata = Post.objects.get(id=article_id)
        mydata.is_published = False
        mydata.save()
        return redirect('/bright/')
    else:
        return redirect('/bright/')
