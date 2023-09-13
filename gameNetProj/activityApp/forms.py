from django import forms

class PostForm(forms.Form):
     textfield = forms.CharField(widget=forms.Textarea(attrs={'class':'post-input','placeholder':'Напишите пост...'}))