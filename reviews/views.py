from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required

from .models import Review
from .forms import ReviewForm


# Create your views here.


def reviews(request):
    """ A view to return the main reviews page """
    posts = reviews.objects.all()
    context = {
        'posts': posts,
    }

    return render(request, 'reviews/reviews.html', context)


def review_detail(request, product_id):
    """ A view that returns individual review posts """
    review_post = get_object_or_404(Review)
    comments = review_post.comments.all()
    new_comment = None

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            # Creates new_comment object (doesn't save it)
            new_comment = review_form.save(commit=False)
            # Assigns the value of what product the user is on
            new_comment.post = review_post
            # Assigns the username (must be logged in to comment)
            new_comment.username = request.user
            new_comment.save()
            messages.info(request, 'Your review has been posted!')
            return redirect(reverse('review_detail', args=[review_post.id]))
        else:
            messages.error(request, 'Failed to post your comment. Check that \
                the form is valid and try again.')
    else:
        review_form = ReviewForm()

    context = {
        'review_post': review_post,
        'comments': comments,
        'review_form': review_form,
    }

    return render(request, 'reviews/review_detail.html', context)
