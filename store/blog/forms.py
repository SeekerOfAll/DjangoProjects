from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from blog.models import Comment, Register

from blog.validators import validate_password, validate_username


class UserLoginForm(forms.Form):
    username = forms.CharField(label=_('نام کاربری'), max_length=150,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label=_('کلمه عبور'), widget=forms.PasswordInput(attrs={'class': 'form-control'}))


# class UserRegistrationForm(forms.Form):
#     username = forms.CharField(label=_('نام کاربری'), max_length=150, required=True,
#                                widget=forms.TextInput(attrs={'class': 'form-control'}))
#     email = forms.EmailField(label=_('ایمیل'), required=True, help_text=_('A valid email for reset your password'),
#                              widget=forms.EmailInput(attrs={'class': 'form-control'}))
#     password = forms.CharField(label=_('کلمه عبور'), required=True,
#                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#     password2 = forms.CharField(label=_('تکرار کلمه عبور'), required=True,
#                                 widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#     first_name = forms.CharField(label=_('نام'), widget=forms.TextInput(attrs={'class': 'form-control'}))
#     last_name = forms.CharField(label=_('نام خانوادگی'), widget=forms.TextInput(attrs={'class': 'form-control'}))
#
#     def clean(self):
#         password = self.cleaned_data.get('password')
#         password2 = self.cleaned_data.get('password2')
#         if password != password2:
#             raise ValidationError(_('Your passwords do not match'), code='invalid')
#
#     def clean_password(self):
#         password = self.cleaned_data.get('password')
#         validate_password(password)
#         return password
#
#     def clean_username(self):
#         username = self.cleaned_data.get('username')
#         validate_username(username)
#         return username

# class UserRegistrationForm(UserCreationForm):
#     email = forms.EmailField()
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'first_name', 'last_name']


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'
        labels = {'username': _('نام کاربری'), 'email': _('ایمیل'), 'password': _('کلمه عبور'),
                  'password2': _('تکرار کلمه عبور'), 'first_name': _('نام'), 'last_name': _('نام خانوادگی'), }
        widget = {'username': forms.TextInput(attrs={'class': 'form-control'}),
                  'email': forms.EmailInput(attrs={'class': 'form-control'}),
                  'password': forms.PasswordInput(attrs={'class': 'form-control'}),
                  'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
                  'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                  'last_name': forms.TextInput(attrs={'class': 'form-control'}), }
        help_text = {'email': _('A valid email for reset your password'), }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        labels = {'content': _('Comment'), }
        help_texts = {'content': _('enter your comment'), }
        widgets = {'content': forms.Textarea}
