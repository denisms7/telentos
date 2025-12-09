from django.contrib import admin

from .models import (
    Skill,
    Talent,
    TalentSkill,
    Certification,
)


class TalentSkillInline(admin.TabularInline):
    model = TalentSkill
    extra = 1
    autocomplete_fields = ("skill",)


@admin.register(Talent)
class TalentAdmin(admin.ModelAdmin):
    list_display = ("user", "job_title", "department", "created_at")
    search_fields = (
        "user__first_name",
        "user__last_name",
        "user__username",
        "job_title",
    )
    autocomplete_fields = ("user",)
    readonly_fields = ("created_at",)
    inlines = (TalentSkillInline,)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "skill_type")
    list_filter = ("skill_type",)
    search_fields = ("name",)


@admin.register(TalentSkill)
class TalentSkillAdmin(admin.ModelAdmin):
    list_display = ("talent", "skill", "level")
    list_filter = ("level", "skill__skill_type")
    autocomplete_fields = ("talent", "skill")


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ("name", "institution", "issue_date", "expiration_date")
    search_fields = ("name", "institution")
