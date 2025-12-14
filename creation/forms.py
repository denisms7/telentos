# accounts/forms.py
from django import forms
from django.contrib.auth import get_user_model
from .models import AccessRequest
from profiles.models import Profile
from .utils import is_valid_cpf, clean_cpf


User = get_user_model()


class AccessRequestForm(forms.ModelForm):

    class Meta:
        model = AccessRequest
        fields = (
            'email',
            'username',
            'full_name',
            'cpf',
            'role',
        )

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')

        if not cpf:
            return cpf

        cpf = clean_cpf(cpf)

        if not is_valid_cpf(cpf):
            raise forms.ValidationError('CPF inválido.')

        if Profile.objects.filter(cpf__iexact=cpf).exists():
            raise forms.ValidationError(
                'Já existe um usuário cadastrado com este CPF.'
            )
        return cpf

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                'Já existe um usuário cadastrado com este e-mail.'
            )
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError(
                'Este usuário já existe.'
            )
        return username
