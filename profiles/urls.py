from django.urls import path

from .views import (
    ProfileDetailView,
)

app_name = "profiles"

urlpatterns = [
    # ===== PERFIL =====
    path("", ProfileDetailView.as_view(), name="home"),
]
