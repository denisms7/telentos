from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import AccessRequestForm
from .models import AccessRequest


class AccessRequestCreateView(CreateView):
    model = AccessRequest
    form_class = AccessRequestForm
    template_name = 'creation/creation.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)

        messages.success(
            self.request,
            'Solicitação enviada com sucesso. '
            'Aguarde a aprovação do administrador.',
        )

        return response

    def form_invalid(self, form):
        messages.error(
            self.request,
            'Não foi possível enviar a solicitação. '
            'Verifique os dados informados.',
        )

        return super().form_invalid(form)
