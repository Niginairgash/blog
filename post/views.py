from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from post.models import Post

User = get_user_model()


class PostListView(ListView):
    template_name = "posts/post_list.html"
    queryset = Post.objects.prefetch_related("tags").filter(is_draft=False)


class PostDetailView(DetailView):
    template_name = "posts/post_detail.html"
    queryset = Post.objects.prefetch_related("tags").filter(is_draft=False)


class UsersPostListView(ListView):
    template_name = "posts/post_list.html"

    def get_username(self):
        return self.request.resolver_match.captured_kwargs.get("username")

    def get_author_or_404(self):
        return get_object_or_404(User, username=self.get_username())

    def get_queryset(self):
        qs = Post.objects.prefetch_related("tags").filter(is_draft=False)
        username = self.get_username()
        if username:
            qs = qs.filter(author__username=username)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["author"] = self.get_author_or_404()
        return context

class SearchListView(ListView):
    template_name = "posts/post_list.html"

    def get_queryset(self):
        qs = Post.objects.prefetch_related("tags").filter(title__contains=self.request.GET.get("search"),
                                 is_draft=False)
        return qs

