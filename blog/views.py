from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .form import UserRegisterForm
from django.contrib.auth import login
from .form import EditUserForm, EditProfileForm
from .form import CommentForm
from django.http import HttpResponseForbidden


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
def edit_profile(request):
    user = request.user
    profile = user.profile

    if request.method == "POST":
        user_form = EditUserForm(request.POST, instance=request.user)
        profile_form = EditProfileForm(
            request.POST, request.FILES, instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("profile")  # change 'profile' to your profile view name
    else:
        user_form = EditUserForm(instance=user)
        profile_form = EditProfileForm(instance=profile)

    return render(
        request,
        "blog/edit_profile.html",
        {"user_form": user_form, "profile_form": profile_form},
    )


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
    comments = post.comments.all().order_by("-created_at")

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post
            new_comment.save()
            return redirect("post_detail", pk=post.pk)
    else:
        comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_form": comment_form,
        },
    )


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


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this comment.")

    post_pk = comment.post.pk
    comment.delete()
    return redirect("post_detail", pk=post_pk)
