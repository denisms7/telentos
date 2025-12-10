from django import forms
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
        fields = (
            "certification_type",
            "name",
            "institution",
            "workload",
            "issue_date",
            "skills",
            "file",
            "link",
        )
        widgets = {
            "issue_date": forms.DateInput(attrs={"type": "date"}),
            "skills": forms.CheckboxSelectMultiple(),
        }
