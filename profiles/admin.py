from django.contrib import admin

from .models import (
    Profile,
    ProfileCertification,
    ProfileSkill,
)


class ProfileSkillInline(admin.TabularInline):
    model = ProfileSkill
    extra = 1
    autocomplete_fields = ("skill",)


class ProfileCertificationInline(admin.TabularInline):
    model = ProfileCertification
    extra = 1
    autocomplete_fields = ("certification",)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "sector",
    )
    search_fields = (
        "user__username",
        "user__first_name",
        "user__last_name",
        "sector",
    )
    list_filter = ("sector",)
    inlines = (
        ProfileSkillInline,
        ProfileCertificationInline,
    )


@admin.register(ProfileSkill)
class ProfileSkillAdmin(admin.ModelAdmin):
    list_display = (
        "profile",
        "skill",
        "level",
        "years_experience",
    )
    list_filter = (
        "level",
        "skill__skill_type",
    )
    search_fields = (
        "profile__user__username",
        "skill__name",
    )
    autocomplete_fields = (
        "profile",
        "skill",
    )


@admin.register(ProfileCertification)
class ProfileCertificationAdmin(admin.ModelAdmin):
    list_display = (
        "profile",
        "certification",
    )
    search_fields = (
        "profile__user__username",
        "certification__name",
    )
    autocomplete_fields = (
        "profile",
        "certification",
    )
