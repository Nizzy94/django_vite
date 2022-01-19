from django.contrib import admin

from blog.models import Category


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("name",)}
#     list_display = ["name", "slug"]
#     # list_filter = ["category"]
#     date_hierarchy = "created_at"
#     exclude = ["created_at", "updated_at"]
