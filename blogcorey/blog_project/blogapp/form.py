from django import forms
from .models import Post

class AddPostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','body']


    

class EditPostForm(AddPostForm):pass