from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from post.views import PostDetailView, PostListView, UsersPostListView, SearchListView

urlpatterns = [
    path("post/", PostListView.as_view(), name="post-list"),
    path("post/<pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/author/<username>/", UsersPostListView.as_view(), name="user-post-list"
    ),
    path("", RedirectView.as_view(url=reverse_lazy("post-list"), permanent=False)),
    path("posts/search/", SearchListView.as_view(), name="search")
]