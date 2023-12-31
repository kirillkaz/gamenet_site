from django import forms 
from .models import Group
from profiles.models import User

class GroupForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.widgets.FileInput(attrs={'class': 'group_avatar', 'accept': 'image/', 'onchange': 'download(this)'}))
    name = forms.CharField(widget=forms.widgets.TextInput(attrs={'class': 'group_name', 'placeholder': 'Название'}))
    description = forms.CharField(widget=forms.widgets.Textarea(attrs={'class': 'group_description', 'placeholder': 'Описание'}))
    # is_private = forms.BooleanField(widget=forms.widgets.Select(
    #     choices=[(True, 'yes'), (False, 'no')],
    #     attrs={'class': 'is_private'}))
    # subscribers = forms.ModelMultipleChoiceField(queryset=User.objects.all())

    class Meta:
        model = Group
        fields = ('avatar', 'name', 'description')