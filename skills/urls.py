from django.urls import path
from .views import SystemListView, SkillListView, FunctionListView

app_name = "skills"

urlpatterns = [
    path("sistemas/", SystemListView.as_view(), name="all_sistemas"),
    path("habilidades/", SkillListView.as_view(), name="all_habilidades"),
    path("cargos/oficiais/", FunctionListView.as_view(), name="all_cargos"),
]
