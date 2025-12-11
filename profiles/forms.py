from django import forms
from django.core.exceptions import ValidationError
from .models import Profile, ProfileSkill, Certification


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


class ProfileSkillForm(forms.ModelForm):
    class Meta:
        model = ProfileSkill
        fields = [
            "skill",
            "level",
            "years_experience",
            "order",
        ]

        widgets = {
            "skill": forms.Select(attrs={"class": "form-select"}),
            "level": forms.Select(attrs={"class": "form-select"}),
            "years_experience": forms.NumberInput(
                attrs={"class": "form-control", "min": 0}
            ),
            "order": forms.NumberInput(
                attrs={"class": "form-control", "min": 0}
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        skill = cleaned_data.get("skill")

        # Evita duplicidade do unique_together(profile, skill)
        if self.instance.pk is None:  # Criando
            profile = self.initial.get("profile") or self.instance.profile
        else:
            profile = self.instance.profile

        if ProfileSkill.objects.filter(
            profile=profile,
            skill=skill
        ).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Essa habilidade já está cadastrada para este perfil.")

        return cleaned_data


class ProfileSkillDetailForm(forms.ModelForm):
    """ Formulário somente leitura para o DetailView """

    class Meta:
        model = ProfileSkill
        fields = [
            "skill",
            "level",
            "years_experience",
            "order",
        ]

        widgets = {
            "skill": forms.TextInput(attrs={"class": "form-control", "readonly": True}),
            "level": forms.TextInput(attrs={"class": "form-control", "readonly": True}),
            "years_experience": forms.NumberInput(
                attrs={"class": "form-control", "readonly": True}
            ),
            "order": forms.NumberInput(
                attrs={"class": "form-control", "readonly": True}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Desabilita todos os campos
        for field in self.fields.values():
            field.disabled = True
