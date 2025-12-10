from django.contrib import admin

from .models import (
    Profile,
    ProfileSkill,
    Certification,
)

class ProfileSkillInline(admin.TabularInline):
    model = ProfileSkill
    extra = 1
    autocomplete_fields = ("skill",)


class CertificationInline(admin.TabularInline):
    model = Certification
    extra = 1
    autocomplete_fields = ("skills",)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "sector")
    search_fields = (
        "user__username",
        "user__first_name",
        "user__last_name",
        "sector",
    )
    list_filter = ("sector",)
    inlines = (
        ProfileSkillInline,
        CertificationInline,
    )

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "profile",
        "certification_type",
        "institution",
        "issue_date",
    )
    list_filter = ("certification_type", "institution")
    search_fields = ("name", "institution", "profile__user__username")
