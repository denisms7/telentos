# accounts/forms.py
from django import forms

from .models import AccessRequest
from .utils import is_valid_cpf


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

        if not is_valid_cpf(cpf):
            raise forms.ValidationError('CPF inválido.')

        return cpf
