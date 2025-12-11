from django.urls import path

from .views import (
    ProfileDetailView,
    CertificationListView,
    CertificationCreateView,
    CertificationDetailView,
    CertificationUpdateView,
    CertificationDeleteView,
)

app_name = "profiles"

urlpatterns = [
    # ===== PERFIL =====
    path("", ProfileDetailView.as_view(), name="home"),


    path("certificados/", CertificationListView.as_view(), name="certificados_list"),
    path("certificados/<int:pk>/", CertificationDetailView.as_view(), name="certificados_det"),
    path("certificados/add/", CertificationCreateView.as_view(), name="certificados_add"),
    path("certificados/<int:pk>/edit", CertificationUpdateView.as_view(), name="certificados_edit"),
    path("certificados/<int:pk>/delete", CertificationDeleteView.as_view(), name="certificados_delete"),
]
