from django.shortcuts import render, get_object_or_404, redirect
from .models import Thread, Post
from .forms import PostForm


def thread_list(request):
    threads = Thread.objects.all()
    return render(request, 'forum/thread_list.html', {'threads': threads})

def thread_detail(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    posts = thread.posts.all()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.author = request.user
            post.save()
            return redirect('thread_detail', pk=thread.pk)
    else:
        form = PostForm()
    return render(request, 'forum/thread_detail.html', {'thread': thread, 'posts': posts, 'form': form})
