from .models import MyUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm


class LoginForm(AuthenticationForm):
    class Meta:
        model = MyUser
        fields = ('email', 'password')


class PersonInfoCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = MyUser
        fields = ('email',)


class PersonInfoChangeForm(UserChangeForm):
    class Meta:
        model = MyUser
        fields = ('email',)
