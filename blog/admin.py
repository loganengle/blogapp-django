from django.contrib import admin
from .models import Category, Post
from django.utils import timezone


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "category",
        "created_at",
        "published_at",
        "updated_at",
    )
    list_filter = ("category", "author", "published_at")
    search_fields = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ("author",)
    date_hierarchy = "published_at"
    ordering = ["-published_at", "-updated_at"]
    readonly_fields = ("created_at", "updated_at", "published_at")

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if obj is None:  # Hide these fields on creation
            fields.remove("created_at")
            fields.remove("updated_at")
            fields.remove("published_at")
        return fields

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # If the object is being created
            obj.created_at = timezone.now()
        if "publish" in form.changed_data and not obj.published_at:
            obj.published_at = (
                timezone.now()
            )  # Set published_at only if publishing for the first time
        obj.updated_at = timezone.now()  # Always update the updated_at field
        obj.author = request.user  # Automatically set the author
        super().save_model(request, obj, form, change)

    def publish_blog(self, request, queryset):
        for post in queryset:
            post.publish()

    actions = [publish_blog]
