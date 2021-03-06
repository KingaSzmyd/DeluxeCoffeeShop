""" Import form, models and widgets """
from django import forms
from products.widgets import CustomClearableFileInput
from .models import BlogPost, Comment


class BlogForm(forms.ModelForm):
    """ The Blog form model """
    class Meta:
        """ The Blog form contains """
        model = BlogPost
        fields = ('title', 'image', 'body',)

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """
        Function sets placeholders, adds auto-focus to top field
        and assigns all fields a class
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'image': 'Image',
            'body': 'Blog Content',
        }

        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = (
                    placeholders[field])
            self.fields[field].widget.attrs['class'] = 'blog-form-input'


class CommentForm(forms.ModelForm):
    """ The comment form model """
    class Meta:
        """ The comment form contains """
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        """
        Function sets placeholder, removes auto-generated input label
        and assigns a class
        """
        super().__init__(*args, **kwargs)
        self.fields['body'].widget.attrs['placeholder'] = (
            'Write your comment here... (500 characters max).')
        self.fields['body'].label = False
        self.fields['body'].widget.attrs['class'] = 'comment-form-input'
