from django.shortcuts import render, redirect
from .models import Post, PostComment
from .forms import PostForm, PostCommentForm
from datetime import datetime
from django.contrib.auth.decorators import login_required


def homepage(request):
    mydata = Post.objects.filter(is_published=True)
    post_form = PostForm()
    return render(request, 'gideon_index.html', {'mycontent': mydata, 'post_form':post_form})


@login_required()
def unpublished_posts(request):
    mydata = Post.objects.filter(is_published=False)
    return render(request, 'gideon_index.html', {'mycontent': mydata})


@login_required()
def post_new_comment(request):
    if request.method == 'POST':
        form = PostCommentForm(request.POST)
        article_id = request.POST.get('article_id')
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = Post.objects.get(id=int(article_id))
            comment.save()
            return redirect('/gideon/')
        else:
            return render(request, 'gideon_post_new_comment.html', {'comment_form': form})


def post_new_comment_form(request):
    article_id = request.POST.get('article_id')
    form = PostCommentForm()
    return render(request, 'gideon_post_new_comment.html', {"article_id": article_id, 'comment_form': form})


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = datetime.now()
            post.save()
            return redirect('/gideon/')
        else:
            return render(request, 'gideon_post_new.html', {'post_form': form})
    else:
        form = PostForm()
        return render(request, 'gideon_post_new.html', {'post_form': form})


def edit_post(request, article_id):
    my_post = Post.objects.get(id=article_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=my_post)
        if form.is_valid():
            post = form.save(commit=False)
            post.modified_date = datetime.now()
            post.save()
            return redirect('/gideon/')
        else:
            return render(request, 'gideon_post_edit.html', {'post_form': form})
    else:
        form = PostForm(instance=my_post)
        return render(request, 'gideon_post_edit.html', {'post_form': form, 'article_id': article_id})


def post_detail(request, article_id):
    mydata = Post.objects.get(id=article_id)
    comments = PostComment.objects.filter(post=mydata)[:1]
    return render(request, 'gideon_post_detail.html', {'myarticle': mydata, "article_id": article_id, "comments":comments})


def delete_post(request, article_id):
    mydata = Post.objects.get(id=article_id)
    mydata.delete()
    return redirect('/gideon/')


def publish_post(request, article_id):
    if request.method == 'POST':
        mydata = Post.objects.get(id=article_id)
        mydata.is_published = True
        mydata.save()

        return redirect('/gideon/')
    else:
        return redirect('/gideon/')


def unpublish_post(request, article_id):
    if request.method == 'POST':
        mydata = Post.objects.get(id=article_id)
        mydata.is_published = False
        mydata.save()

        return redirect('/gideon/')
    else:
        return redirect('/gideon/')




