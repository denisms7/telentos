from django.contrib import admin
from .models import Skill, System, Function


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "skill_type")
    list_filter = ("skill_type",)
    search_fields = ("name",)
    readonly_fields = ("created_at",)


@admin.register(System)
class SystemAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "active",
        "created_at",
    )
    list_filter = ("active",)
    search_fields = ("name", "description",)
    ordering = ("name",)
    readonly_fields = ("created_at",)


@admin.register(Function)
class FunctionAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    readonly_fields = ("created_at",)
