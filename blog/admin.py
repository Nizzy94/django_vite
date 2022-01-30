from django.contrib import admin
from PIL import Image
from .models import Blog, Category, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "slug"]
    # list_filter = ["category"]
    date_hierarchy = "created_at"
    exclude = ["created_at", "updated_at"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "slug"]
    # list_filter = ["category"]
    date_hierarchy = "created_at"
    exclude = ["created_at", "updated_at"]


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    # prepopulated_fields = {"slug": ("title",)}
    list_display = ["title", "author"]
    list_filter = ["category", "tags"]
    date_hierarchy = "created_at"
    exclude = ["created_at", "updated_at", 'author', 'slug']

    def save_model(self, request, obj, form, change):
        print({
            # 'req': request.POST.get(),
            'obj': obj,
            'form':  form,
            'change': change
        })
        if not change:
            obj.author = request.user

        super(BlogAdmin, self).save_model(request, obj, form, change)
