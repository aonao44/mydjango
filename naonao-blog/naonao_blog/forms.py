from dataclasses import field, fields
import imp
from django import forms

from naonao_blog.models import Comment, Reply


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'text')
        widgets = {
            'nama': forms.Textarea(attrs={'placeholeder': 'name'}),
            'text': forms.Textarea(attrs={'placeholder': 'please enter your comment...'}),
        }


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('name', 'text')
        widgets = {
            'nama': forms.Textarea(attrs={'placeholeder': 'name'}),
            'text': forms.Textarea(attrs={'placeholder': 'please reply...'}),
        }
