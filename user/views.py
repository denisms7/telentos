from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView
from django.views.generic import DetailView, TemplateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import UsuarioSenhaForm, Usuario_UserForm
from django.contrib.auth import views as auth_views
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin


class UsuarioEdit(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = User
    form_class = UsuarioSenhaForm
    template_name = 'accounts/alterar_senha.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        update_session_auth_hash(self.request, user)
        messages.success(self.request, 'Sua senha foi alterada com sucesso!')
        return super().form_valid(form)


class UsuarioDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = User
    template_name = 'accounts/perfil.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['groups'] = user.groups.all()
        context['last_login'] = user.last_login
        context['date_joined'] = user.date_joined
        context['user_permissions'] = user.user_permissions.all()
        context['group_permissions'] = user.get_group_permissions()  # opcional

        return context


@user_passes_test(lambda user: user.is_authenticated)
def alterar_usuario(request):
    if request.method == 'POST':
        form = Usuario_UserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dados do usuário foram alterados com sucesso.')
            return redirect('alterar_usuario')
    else:
        form = Usuario_UserForm(instance=request.user)

    context = {
        'form': form
    }
    return render(request, 'accounts/alterar_usuario.html', context)


class AcessoNegadoView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/acesso_negado.html'


class CustomPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    def get(self, request, *args, **kwargs):
        messages.success(request, "Senha redefinida com sucesso! Faça login com a nova senha.")
        return redirect(reverse_lazy("login"))
