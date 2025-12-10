from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    ListView,
    TemplateView,
)

from .models import Profile, ProfileSkill, Certification, Skill


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "profiles/profile_detail.html"

    def get_object(self):
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["certifications"] = self.object.certifications.order_by("-issue_date")
        return context
