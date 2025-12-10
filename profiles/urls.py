from django.urls import path

from .views import (
    ProfileDetailView,
    ProfileUpdateView,
    CertificationCreateView,
    CertificationListView,
    ProfileSkillManageView,
    toggle_profile_skill,
)

app_name = "profiles"

urlpatterns = [
    # ===== PERFIL =====
    path("detalhe/", ProfileDetailView.as_view(), name="detail"),
    path("editar/", ProfileUpdateView.as_view(), name="edit"),

    # ===== SKILLS (GERENCIAR – DRAG & DROP) =====
    path(
        "skills/",
        ProfileSkillManageView.as_view(),
        name="skills-manage",
    ),
    path(
        "skills/toggle/",
        toggle_profile_skill,
        name="skills-toggle",
    ),

    # ===== CERTIFICADOS =====
    path(
        "certificados/",
        CertificationListView.as_view(),
        name="certification_list",
    ),
    path(
        "certificados/adicionar/",
        CertificationCreateView.as_view(),
        name="certification_add",
    ),
]
