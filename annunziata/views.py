from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm
from django.utils import timezone
# Create your views here.
def home(request):
    myposts = Post.objects.all()
    return render(request, 'annunziata_index.html', {'myposts': myposts})

def post_detail(request, post_id):
    postdata = Post.objects.get(id=post_id)
    return render(request, 'annunziata_post_detail.html', {'postdata': postdata})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('/annunziata/')
        else:
            return render(request, 'annunziata_post_new.html', {'post_form': form})
    else:
        form = PostForm()
        return render(request, 'annunziata_post_new.html', {'post_form': form})