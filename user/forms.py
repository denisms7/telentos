from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class UsuarioSenhaForm(forms.ModelForm):
    password_antiga = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha atual'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Nova senha'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme sua senha'}))

    class Meta:
        model = User
        fields = ['password_antiga', 'password', 'password1']

    def clean_password1(self):
        password = self.cleaned_data.get('password')
        password1 = self.cleaned_data.get('password1')
        if password and password1 and password != password1:
            raise forms.ValidationError("As senhas não são iguais.")
        return password1

    def clean_password_antiga(self):
        password_antiga = self.cleaned_data.get('password_antiga')
        if not self.instance.check_password(password_antiga):
            raise forms.ValidationError("A senha antiga está incorreta.")
        return password_antiga


class Usuario_UserForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
        )
