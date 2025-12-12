from django.views.generic import ListView
from .models import System, Skill, SkillType
from django.db.models import Q


class SystemListView(ListView):
    model = System
    template_name = "skills/system_list.html"
    context_object_name = "systems"
    paginate_by = 20

    def get_queryset(self):
        queryset = System.objects.filter(active=True)

        q = self.request.GET.get("q")
        if q:
            queryset = queryset.filter(Q(name__icontains=q) | Q(description__icontains=q))
        return queryset


class SkillListView(ListView):
    model = Skill
    template_name = "skills/skill_list.html"
    context_object_name = "skills"
    paginate_by = 20

    def get_queryset(self):
        queryset = Skill.objects.filter(active=True)

        # filtro de busca
        q = self.request.GET.get("q")
        if q:
            queryset = queryset.filter(name__icontains=q)

        # filtro por tipo
        skill_type = self.request.GET.get("skill_type")
        if skill_type:
            queryset = queryset.filter(skill_type=skill_type)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["skill_types"] = SkillType.choices
        return context
