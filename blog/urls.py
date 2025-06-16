from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
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
