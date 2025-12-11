from django.urls import path

from .views import (
    ProfileDetailView,
    CertificationListView,
    CertificationCreateView,
    CertificationDetailView,
    CertificationUpdateView,
    CertificationDeleteView,

    ProfileSkillListView,
    ProfileSkillCreateView,
    ProfileSkillDetailView,
    ProfileSkillUpdateView,
    ProfileSkillDeleteView,

)

app_name = "profiles"

urlpatterns = [
    # ===== PERFIL =====
    path("", ProfileDetailView.as_view(), name="home"),

    #  Certificados
    path("certificados/", CertificationListView.as_view(), name="certificados_list"),
    path("certificados/<int:pk>/", CertificationDetailView.as_view(), name="certificados_det"),
    path("certificados/add/", CertificationCreateView.as_view(), name="certificados_add"),
    path("certificados/<int:pk>/edit", CertificationUpdateView.as_view(), name="certificados_edit"),
    path("certificados/<int:pk>/delete", CertificationDeleteView.as_view(), name="certificados_delete"),

    # Habilidades
    path("habilidades/", ProfileSkillListView.as_view(), name="habilidades_list"),
    path("habilidades/novo/", ProfileSkillCreateView.as_view(), name="habilidades_create"),
    path("habilidades/<int:pk>/", ProfileSkillDetailView.as_view(), name="habilidades_detail"),
    path("habilidades/<int:pk>/editar/", ProfileSkillUpdateView.as_view(), name="habilidades_update"),
    path("habilidades/<int:pk>/excluir/", ProfileSkillDeleteView.as_view(), name="habilidades_delete"),




]
