from django.contrib import admin
from .models import Profile, Certification


class CertificationInline(admin.TabularInline):
    model = Certification
    extra = 1
    fields = (
        "name",
        "certification_type",
        "institution",
        "issue_date",
    )
    show_change_link = True


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "position",
    )
    search_fields = (
        "user__username",
        "user__first_name",
        "user__last_name",
        "position",
    )
    list_filter = (
        "position",
    )
    inlines = (
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
    list_filter = (
        "certification_type",
        "institution",
    )
    search_fields = (
        "name",
        "institution",
        "profile__user__username",
        "profile__user__first_name",
        "profile__user__last_name",
    )
    autocomplete_fields = (
        "profile",
    )
