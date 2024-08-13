from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(
        max_length=100,
        unique=True,
        help_text="A short label for the category, used in URLs.",
    )

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=200,
        unique=True,
        help_text="A short label for the post, used in URLs.",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blog_posts",
        help_text="The user who authored the post.",
    )
    body = models.TextField(help_text="The content of the blog post.")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="posts",
        help_text="The category of the blog post.",
    )
    created_at = models.DateTimeField(
        default=timezone.now, help_text="The date and time when the post was created."
    )
    updated_at = models.DateTimeField(
        auto_now=True, help_text="The date and time when the post was last updated."
    )
    published_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text="The date and time when the post was published.",
    )

    def __str__(self):
        return self.title

    def publish(self):
        """Publish the post by setting the `published_at` field to the current time if not already set."""
        if self.published_at is None:
            self.published_at = timezone.now()
        self.save()

    def is_published(self):
        """Check if the post is published."""
        return self.published_at is not None

    class Meta:
        ordering = [
            "-published_at",
            "-updated_at",
        ]  # Order by published_at first, then updated_at
