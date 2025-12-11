from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.db.models import Q
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.db.models.deletion import ProtectedError, RestrictedError
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    ListView,
    TemplateView,
    DeleteView,
)


from .models import Profile, Certification, CertificationType, ProfileSkill, SkillLevel
from skills.models import SkillType

from .forms import CertificationForm, CertificationDetail_ModelForm
from .forms import ProfileSkillForm, ProfileSkillDetailForm

class ProfileDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Profile
    template_name = "profiles/profile_detail.html"
    permission_required = 'register.view_certification'

    def get_object(self):
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["certifications"] = self.object.certifications.order_by("-issue_date")
        return context


class CertificationListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = "certification/certification_list.html"
    context_object_name = "certifications"
    permission_required = 'register.view_certification'
    paginate_by = 10

    def get_queryset(self):
        profile = self.request.user.profile

        queryset = profile.certifications.all()

        q = self.request.GET.get("q")
        if q:
            queryset = queryset.filter(
                Q(name__icontains=q) | Q(institution__icontains=q)
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


class CertificationCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Certification
    form_class = CertificationForm
    template_name = "certification/certification_create.html"
    success_url = reverse_lazy("profiles:certificados_list")
    permission_required = 'register.add_certification'

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        messages.success(self.request, "Certificado cadastrado com sucesso!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Erro ao salvar o certificado. Verifique os campos e tente novamente.")
        return super().form_invalid(form)


class CertificationDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Certification
    template_name = "certification/certification_create.html"
    context_object_name = "certification"
    permission_required = 'register.view_certification'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CertificationDetail_ModelForm(instance=self.object)
        context["is_detail"] = True
        return context


class CertificationUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Certification
    form_class = CertificationForm
    template_name = "certification/certification_create.html"  # ou certification_update.html
    context_object_name = "certification"
    success_url = reverse_lazy("profiles:certificados_list")
    permission_required = 'register.change_certification'

    def get_queryset(self):
        # Garante que o usuário só pode editar certificados do próprio perfil
        return Certification.objects.filter(profile=self.request.user.profile)

    def form_valid(self, form):
        messages.success(self.request, "Certificado atualizado com sucesso!")
        return super().form_valid(form)


class CertificationDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Certification
    template_name = "certification/certification_delete.html"
    context_object_name = "certification"
    success_url = reverse_lazy("profiles:certificados_list")
    permission_required = 'register.delete_certification'

    def get_queryset(self):
        # Garante que o usuário só apague seus próprios certificados
        return Certification.objects.filter(profile=self.request.user.profile)

    def delete(self, request, *args, **kwargs):
            self.object = self.get_object()

            try:
                self.object.delete()
                messages.success(request, "Certificado deletado com sucesso.")

            except ProtectedError:
                messages.warning(
                    request,
                    "Este certificado não pode ser deletado pois existem dados vinculados."
                )

            except RestrictedError:
                messages.warning(
                    request,
                    "Este certificado possui vínculos restritos e não pode ser deletado."
                )

            except Exception:
                messages.error(
                    request,
                    "Ocorreu um erro ao tentar deletar o certificado."
                )

            return redirect(self.success_url)






# ================================ SKILLS ================================


class ProfileSkillListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = "skills/skill_list.html"
    context_object_name = "skills"
    paginate_by = 10
    permission_required = "register.view_profileskill"

    def get_queryset(self):
        profile = self.request.user.profile
        queryset = profile.skills.all()

        q = self.request.GET.get("q")
        if q:
            queryset = queryset.filter(
                Q(skill__name__icontains=q)
            )

        level = self.request.GET.get("level")
        if level:
            queryset = queryset.filter(level=level)

        skill_type = self.request.GET.get("skill_type")
        if skill_type:
            queryset = queryset.filter(skill__skill_type=skill_type)

        return queryset.order_by("order", "skill__name")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["levels"] = SkillLevel.choices
        context["skill_types"] = SkillType.choices

        params = self.request.GET.copy()
        params.pop("page", None)

        context["querystring"] = params.urlencode()

        return context








class ProfileSkillCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = ProfileSkill
    form_class = ProfileSkillForm
    template_name = "skills/skill_create.html"
    success_url = reverse_lazy("profiles:skills_list")
    permission_required = "register.add_profileskill"

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        messages.success(self.request, "Habilidade adicionada com sucesso!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            "Erro ao salvar a habilidade. Verifique os campos e tente novamente."
        )
        return super().form_invalid(form)


class ProfileSkillDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = ProfileSkill
    template_name = "skills/skill_create.html"
    context_object_name = "skill"
    permission_required = "register.view_profileskill"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ProfileSkillDetailForm(instance=self.object)
        context["is_detail"] = True
        return context


class ProfileSkillUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = ProfileSkill
    form_class = ProfileSkillForm
    template_name = "skills/skill_create.html"
    context_object_name = "skill"
    success_url = reverse_lazy("profiles:skills_list")
    permission_required = "register.change_profileskill"

    def get_queryset(self):
        return ProfileSkill.objects.filter(profile=self.request.user.profile)

    def form_valid(self, form):
        messages.success(self.request, "Habilidade atualizada com sucesso!")
        return super().form_valid(form)


class ProfileSkillDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = ProfileSkill
    template_name = "skills/profile_skill_delete.html"
    context_object_name = "skill"
    success_url = reverse_lazy("profiles:skills_list")
    permission_required = "register.delete_profileskill"

    def get_queryset(self):
        return ProfileSkill.objects.filter(profile=self.request.user.profile)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()

        try:
            self.object.delete()
            messages.success(request, "Habilidade removida com sucesso.")

        except ProtectedError:
            messages.warning(
                request,
                "Esta habilidade não pode ser deletada pois possui vínculos protegidos."
            )

        except RestrictedError:
            messages.warning(
                request,
                "Esta habilidade possui vínculos restritos e não pode ser deletada."
            )

        except Exception:
            messages.error(
                request,
                "Ocorreu um erro ao tentar deletar a habilidade."
            )

        return redirect(self.success_url)

