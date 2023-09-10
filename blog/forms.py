from django import forms
from .models import BlogPost, BlogFeedback
from category.models import Category


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'description', 'categories', 'status', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize widgets with Bootstrap classes
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'write description here..', 'rows': 4})
        self.fields['categories'].widget.attrs.update(
            {'class': 'form-control'})

        # Add attributes to the status and image fields as needed
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'form-control'


class BlogFeedbackForm(forms.ModelForm):
    class Meta:
        model = BlogFeedback
        fields = ['rating', 'review']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['rating'].widget.attrs.update({'class': 'form-control'})
        self.fields['review'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'write your review here..', 'rows': 4})
