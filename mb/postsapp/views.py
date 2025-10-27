from django.views.generic import ListView
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'  # template to render
    context_object_name = 'all_posts_list'  # name to use in template

from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

def home(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()

    posts = Post.objects.all()
    return render(request, 'home.html', {'form': form, 'all_posts_list': posts})