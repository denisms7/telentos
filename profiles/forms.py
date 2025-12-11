from django import forms
from django.core.exceptions import ValidationError
from .models import Profile, ProfileSkill, Certification


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ("position",)


class ProfileSkillForm(forms.ModelForm):

    class Meta:
        model = ProfileSkill
        fields = (
            "skill",
            "level",
            "years_experience",
        )


class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = [
            "certification_type",
            "name",
            "institution",
            "workload",
            "issue_date",
            "file",
            "link",
        ]
        widgets = {
            "issue_date": forms.DateInput(
                format="%Y-%m-%d",
                attrs={"type": "date"}
            ),
        }


class CertificationDetail_ModelForm(forms.ModelForm):

    class Meta:
        model = Certification
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs["readonly"] = True  # impede edição
            field.widget.attrs["disabled"] = True  # evita submissão
