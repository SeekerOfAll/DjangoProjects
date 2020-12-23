from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


def validate_password(password):
    if len(password) < 5:
        raise ValidationError(_('Your password is short'), code='invalid')
    return password


def validate_username(username):
    try:
        User.objects.get(username=username)
        raise ValidationError(_('this username already exist'))
    except User.DoesNotExist:
        pass
    return username
