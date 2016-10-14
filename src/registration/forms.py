from __future__ import unicode_literals


from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as dj_User

from .users import UserModel, UsernameField
from .models import RegistrationProfile

User = UserModel()


class RegistrationForm(UserCreationForm):
    required_css_class = 'required'
    email = forms.EmailField(label=_("E-mail"))

    class Meta:
        model = User
        fields = (UsernameField(), "email")


class RegistrationFormTermsOfService(RegistrationForm):
    tos = forms.BooleanField(widget=forms.CheckboxInput,
                             label=_('I have read and agree to the Terms of Service'),
                             error_messages={'required': _("You must agree to the terms to register")})


class RegistrationFormUniqueEmail(RegistrationForm):
    def clean_email(self):
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
        return self.cleaned_data['email']


class RegistrationFormNoFreeEmail(RegistrationForm):
    bad_domains = ['aim.com', 'aol.com', 'email.com', 'gmail.com',
                   'googlemail.com', 'hotmail.com', 'hushmail.com',
                   'msn.com', 'mail.ru', 'mailinator.com', 'live.com',
                   'yahoo.com']

    def clean_email(self):
        email_domain = self.cleaned_data['email'].split('@')[1]
        if email_domain in self.bad_domains:
            raise forms.ValidationError(_("Registration using free email addresses is prohibited. Please supply a different email address."))
        return self.cleaned_data['email']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = dj_User
        fields = ('username', 'first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = RegistrationProfile
        fields = ('date_of_birth',)
