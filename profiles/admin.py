from django.contrib import admin
from .models import Profile, ProfileSkill, ProfileSystem

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "position")
    search_fields = (
        "user__username",
        "user__first_name",
        "user__last_name",
        "position",
    )


@admin.register(ProfileSystem)
class ProfileSystemAdmin(admin.ModelAdmin):
    list_display = ("profile", "system", "access_level", "notes_short")
    search_fields = (
        "profile__user__username",
        "profile__user__first_name",
        "profile__user__last_name",
        "system__name",
        "access_level",
        "notes",
    )
    list_filter = ("system", "access_level")
    autocomplete_fields = ("profile", "system")

    def notes_short(self, obj):
        """Mostra só os primeiros caracteres das observações."""
        if not obj.notes:
            return "—"
        return obj.notes[:40] + "..." if len(obj.notes) > 40 else obj.notes

    notes_short.short_description = "Observações"


@admin.register(ProfileSkill)
class ProfileSkillAdmin(admin.ModelAdmin):
    list_display = (
        "profile",
        "skill",
        "level",
        "years_experience",
        "order",
    )

    list_filter = (
        "level",
        "profile",
        "skill",
    )

    search_fields = (
        "profile__user__username",
        "profile__user__first_name",
        "profile__user__last_name",
        "skill__name",
    )