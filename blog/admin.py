""" Import django libraries and app models """
from django.contrib import admin
from .models import BlogPost, Comment

# Register your models here.


class BlogPostAdmin(admin.ModelAdmin):
    """ Admin has an access to the Blog """
    list_display = ('date_posted', 'title', 'slug')
    search_fields = ['title', 'content']


class CommentAdmin(admin.ModelAdmin):
    """ Admin has an access to the Blog Comments """
    list_display = ('date_posted', 'post', 'body', 'username')
    search_fields = ['username', 'body']


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment, CommentAdmin)
