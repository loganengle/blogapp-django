from django import forms
from django.contrib import admin
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "slug", "body", "category", "published_at"]

    def save(self, commit=True):
        post = super().save(commit=False)
        if not post.author_id:
            post.author = self.current_user
        if commit:
            post.save()
        return post


class PostAdmin(admin.ModelAdmin):
    form = PostForm

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.current_user = request.user
        return form
