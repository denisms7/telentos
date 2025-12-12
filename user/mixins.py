from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy


class GrupoRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    grupos_permitidos = []  # lista de strings
    login_url = reverse_lazy('login')
    redirect_url = reverse_lazy('acesso-negado')
    
    def test_func(self):
        user = self.request.user
        if user.is_superuser:
                    return True
        grupos_usuario = user.groups.values_list('name', flat=True)
        return bool(set(self.grupos_permitidos) & set(grupos_usuario))

    def handle_no_permission(self):
        next_url = self.request.META.get('HTTP_REFERER')
        if self.request.user.is_authenticated:
            if next_url:
                messages.warning(self.request, "Você não tem permissão para acessar esta página.")   
                return redirect(next_url)
            return redirect(self.redirect_url)
        return super().handle_no_permission()
    