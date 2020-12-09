from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from userreg.models import Profile
from django.contrib.auth.models import User

def posts_of_following_profiles(request):
    #first user will login
    profile = Profile.objects.get(user=request.user)
    #look at followers list
    users = [user for user in profile.following.all()]
    #intial values
    postss = []
    #now we get the posts
    for u in users:
        p = Profile.objects.get(user=u)
        p_posts = p.post_set.all()
        postss.append(p_posts)
    #my own posts
    my_posts = profile.profiles_posts()
    postss.append(my_posts)
    return render(request, 'blog/main.html', {'profile': profile, 'postss': postss})

def home(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'caption', 'imgg']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'caption', 'imgg']

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False




    
