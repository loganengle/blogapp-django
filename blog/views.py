from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Post


def home(request):
    query = request.GET.get("query", "")
    if query:
        post_list = (
            Post.objects.filter(
                Q(title__icontains=query)
                | Q(body__icontains=query)
                | Q(author__username__icontains=query)
            )
            .filter(published_at__isnull=False)
            .order_by("-published_at")
        )
    else:
        post_list = Post.objects.filter(published_at__isnull=False).order_by(
            "-published_at"
        )

    paginator = Paginator(post_list, 3)  # Show 3 posts per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "home.html", {"page_obj": page_obj, "query": query})


def view_post(request, slug):
    """
    View to display a single blog post.
    """
    post = get_object_or_404(Post, slug=slug)
    if post.is_published():
        return render(request, "view_post.html", {"post": post})
    else:
        return redirect("home")
