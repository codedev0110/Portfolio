from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'published')
    list_filter = ('published', 'created_at')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}