from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import DetailView, TemplateView
from profiles.models import Profile


class HomeDetailView(TemplateView):
    template_name = "home/home.html"


class ProfileDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Profile
    template_name = "home/profile.html"
    permission_required = 'register.view_certification'

    def get_object(self):
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["certifications"] = self.object.certifications.order_by("-issue_date")
        return context
