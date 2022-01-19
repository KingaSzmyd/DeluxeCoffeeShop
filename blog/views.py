from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.utils.text import slugify

from .models import BlogPost
from .forms import BlogForm, CommentForm

# Create your views here.


def blog_posts(request):
    """ A view to return the main blog page """
    posts = BlogPost.objects.all()
    context = {
        'posts': posts,
    }

    return render(request, 'blog/blog.html', context)


def blog_detail(request, slug):
    """ A view that returns individual blog posts """
    blog_post = get_object_or_404(BlogPost, slug=slug)
    comments = blog_post.comments.all()
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = blog_post
            new_comment.username = request.user
            new_comment.save()
            messages.info(request, 'Your comment has been posted!')
            return redirect(reverse('blog_detail', args=[blog_post.slug]))
        else:
            messages.error(request, 'Failed to post your comment. Check that \
                the post is valid and try again.')
    else:
        comment_form = CommentForm()

    context = {
        'blog_post': blog_post,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'blog/blog_detail.html', context)
