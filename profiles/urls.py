from django.urls import path

from .views import (
    ProfileDetailView,
    CertificationListView,
)

app_name = "profiles"

urlpatterns = [
    # ===== PERFIL =====
    path("", ProfileDetailView.as_view(), name="home"),


    path("certificados", CertificationListView.as_view(), name="certificados"),
]
