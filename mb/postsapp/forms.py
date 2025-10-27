from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows':4, 'cols':40, 'placeholder':'Write your message here...'}),
        }