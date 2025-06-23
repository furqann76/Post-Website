from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib import admin
from blog import views as blog_views
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from .views import PostListAPIView


def redirect_to_login(request):
    return redirect("login")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/posts/", PostListAPIView.as_view(), name="api-post-list"),
    path("register/", blog_views.register, name="register"),  # type: ignore
    path("profile/", blog_views.profile, name="profile"),  # type: ignore
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("search/", views.search_posts, name="search"),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
    path("my_posts/", views.my_posts, name="my_posts"),
    path(
        "comment/<int:comment_id>/delete/", views.delete_comment, name="delete_comment"
    ),
    path('speak-comment/<int:comment_id>/', views.speak_comment, name='speak_comment'),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="blog/login.html"),
        name="login",
    ),
    path("", views.home, name="home"),
    path("post/<int:pk>", views.post_detail, name="post-detail"),
    path("post/new/", views.PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/edit/", views.PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post-delete"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
