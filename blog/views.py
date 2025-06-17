from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .form import UserRegisterForm
from django.contrib.auth import login


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()  # This now properly handles profile creation
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            login(request, user)
            return redirect("home")  # Changed from 'login' to 'home' for better UX
    else:
        form = UserRegisterForm()
    return render(request, "blog/register.html", {"form": form, "title": "Register"})


@login_required
def profile(request):
    return render(request, "blog/profile.html", {"title": "Profile"})


# Create your views here.
@login_required
def home(request):
    posts = Post.objects.all()
    return render(request, "blog/home.html", {"posts": posts})


# View Details
@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})


# Create Post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("home")


# Update Post
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("home")


# Delete Post
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("home")
