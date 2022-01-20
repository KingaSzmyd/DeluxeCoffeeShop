from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.utils.text import slugify

from .models import ReviewPost
from .forms import ReviewForm


# Create your views here.


def review_posts(request):
    """ A view to return the main reviews page """
    posts = ReviewPost.objects.all()
    context = {
        'posts': posts,
    }

    return render(request, 'reviews/reviews.html', context)


def review_detail(request, slug):
    """ A view that returns individual review posts """
    review_post = get_object_or_404(ReviewPost, slug=slug)
    comments = review_post.comments.all()
    new_comment = None

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            new_comment = review_form.save(commit=False)
            new_comment.post = review_post
            new_comment.username = request.user
            new_comment.save()
            messages.info(request, 'Your review has been posted!')
            return redirect(reverse('review_detail', args=[review_post.slug]))
        else:
            messages.error(request, 'Failed to post your review. Check that \
                the form is valid and try again.')  
    else:
        review_form = ReviewForm()

    context = {
        'review_post': review_post,
        'comments': comments,
        'review_form': review_form,
    }

    return render(request, 'reviews/review_detail.html', context)
