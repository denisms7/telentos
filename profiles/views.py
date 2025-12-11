from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    ListView,
    TemplateView,
)

from .models import Profile, Certification, CertificationType


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "profiles/profile_detail.html"

    def get_object(self):
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["certifications"] = self.object.certifications.order_by("-issue_date")
        return context


class CertificationListView(LoginRequiredMixin, ListView):
    template_name = "certification/certification_list.html"
    context_object_name = "certifications"
    paginate_by = 10

    def get_queryset(self):
        profile = self.request.user.profile

        queryset = profile.certifications.all()

        q = self.request.GET.get("q")
        if q:
            queryset = queryset.filter(
                Q(name__icontains=q) |
                Q(institution__icontains=q)
            )

        cert_type = self.request.GET.get("type")
        if cert_type:
            queryset = queryset.filter(certification_type=cert_type)

        return queryset.order_by("-issue_date")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["types"] = CertificationType.choices

        params = self.request.GET.copy()
        if "page" in params:
            params.pop("page")

        context["querystring"] = params.urlencode()

        return context
