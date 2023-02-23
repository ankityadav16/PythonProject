from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import forms
from django import forms

class UserSignUpForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username','email','password1','password2')
        

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'input100','placeholder':"Type your username"})
        self.fields['email'].widget.attrs.update({'class': 'input100','placeholder':"Type your email"})
        self.fields['password1'].widget.attrs.update({'class': 'input100','placeholder':"Type your password"})
        self.fields['password2'].widget.attrs.update({'class': 'input100','placeholder':"Confirm password"})
        

        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].label = ''


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100','placeholder':"Type your username",'data-validate' : "Username is required"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100','placeholder':"Type your password",'data-validate' : "Username is required"}))

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['password'].label = ''