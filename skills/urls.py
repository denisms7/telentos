from django.urls import path
from .views import SystemListView,SkillListView

app_name = "skills"

urlpatterns = [
    path("sistemas/", SystemListView.as_view(), name="all_sistemas"),
    path("habilidades/", SkillListView.as_view(), name="all_habilidades"),
]
