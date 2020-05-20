from django import forms
from .models import Post, PostComment

class PostForm(forms.ModelForm):

    title = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={'class': "form-control"}))

    content = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': "form-control"}))

    class Meta:
        model = Post
        fields = ('title', 'content', 'image')


class PostCommentForm(forms.ModelForm):

    comment = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': "form-control"}))

    class Meta:
        model = PostComment
        fields = ('comment', )
