from django import forms
from src.pages.models import PageInfo, PostOnPage, Message


class ProfileInfoForm(forms.ModelForm):
    profile_image = forms.ImageField(required=None)
    age = forms.IntegerField(required=None)

    class Meta:
        model = PageInfo
        fields = [
            'first_name',
            'last_name',
            'age',
            'profile_image',
        ]


class PostInfoForm(forms.ModelForm):
    post = forms.CharField(required=None)
    post_Img = forms.ImageField(required=None)

    class Meta:
        model = PostOnPage
        fields = ['post', 'post_Img']


class SendMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['msg_content']