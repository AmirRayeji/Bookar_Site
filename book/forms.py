from django import forms

from book.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('text',)

