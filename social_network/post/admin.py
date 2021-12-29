from django.contrib import admin

from .models import Post, Like


class LikeInline(admin.TabularInline):
    model = Like
    extra = 0


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ['author', 'body', 'created_at', 'updated_at', 'likes']


admin.site.register(Post, PostAdmin)
