from django import forms
from comment.models import Comment

class CommentForm(forms.ModelForm):
	body = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}), required=True)

	class Meta:
		model = Comment
		fields = ('body',)