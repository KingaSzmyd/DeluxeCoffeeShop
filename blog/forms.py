from django import forms
from products.widgets import CustomClearableFileInput
from .models import BlogPost, Comment


class BlogForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'image': 'Image',
            'content': 'Blog Content',
        }

        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = (
                    placeholders[field])
            self.fields[field].widget.attrs['class'] = 'blog-form-input'
            field.widget.attrs['class'] = 'border-black rounded-0'


class CommentForm(forms.ModelForm):

    class Meta:
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
