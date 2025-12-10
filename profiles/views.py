from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    ListView,
    TemplateView,
)
import json

from .models import Profile, ProfileSkill, Certification, Skill
from .forms import (
    ProfileForm,
    ProfileSkillForm,
    CertificationForm,
)




from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404






class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "profiles/profile_detail.html"

    def get_object(self):
        return self.request.user.profile


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "profiles/profile_form.html"
    success_url = reverse_lazy("profiles:detail")

    def get_object(self):
        return self.request.user.profile



class CertificationListView(LoginRequiredMixin, ListView):
    model = Certification
    template_name = "profiles/certification_list.html"

    def get_queryset(self):
        return Certification.objects.filter(
            profile=self.request.user.profile
        )


class CertificationCreateView(LoginRequiredMixin, CreateView):
    model = Certification
    form_class = CertificationForm
    template_name = "profiles/certification_form.html"
    success_url = reverse_lazy("profiles:certification_list")

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)


class ProfileSkillCreateView(LoginRequiredMixin, CreateView):
    model = ProfileSkill
    form_class = ProfileSkillForm
    template_name = "profiles/profile_skill_form.html"

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "profiles:detail",
            kwargs={"pk": self.request.user.profile.pk},
        )



@login_required
@require_POST
def toggle_profile_skill(request):
    data = json.loads(request.body)
    skill_id = data.get("skill_id")

    profile = request.user.profile
    skill = Skill.objects.get(id=skill_id)

    obj, created = ProfileSkill.objects.get_or_create(
        profile=profile,
        skill=skill,
        defaults={"level": "basic", "years_experience": 0},
    )

    if not created:
        obj.delete()
        return JsonResponse({"status": "removed"})

    return JsonResponse({"status": "added"})



class ProfileSkillManageView(LoginRequiredMixin, TemplateView):
    template_name = "profiles/profile_skill_manage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        profile = self.request.user.profile

        user_skills = ProfileSkill.objects.filter(
            profile=profile,
        ).select_related("skill").order_by("order")

        user_skill_ids = user_skills.values_list("skill_id", flat=True)

        available_skills = Skill.objects.exclude(
            id__in=user_skill_ids,
        ).order_by("name")

        context["user_skills"] = user_skills
        context["available_skills"] = available_skills

        return context