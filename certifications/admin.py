from django.contrib import admin
from .models import (
    Skill,
    Certification,
    System,
)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "skill_type")
    list_filter = ("skill_type",)
    search_fields = ("name",)


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "certification_type",
        "institution",
        "issue_date",
    )
    list_filter = ("certification_type", "institution")
    search_fields = ("name", "institution")


@admin.register(System)
class SystemAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "owner_sector",
        "active",
        "created_at",
    )
    list_filter = ("active", "owner_sector")
    search_fields = ("name", "description", "owner_sector")
    ordering = ("name",)
    readonly_fields = ("created_at",)
