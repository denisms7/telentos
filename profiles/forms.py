from django import forms
from .models import ProfileSkill, Certification, Profile, ProfileSystem


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "function",
            "registration",
            "admission_date",
            "public",
        ]
        widgets = {
            "admission_date": forms.DateInput(
                format="%Y-%m-%d",
                attrs={"type": "date"}
            ),
        }


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
    def __init__(self, *args, **kwargs):
        self.profile = kwargs.pop("profile", None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = ProfileSkill
        fields = [
            "skill",
            "level",
            "notes",
        ]

    def clean(self):
        cleaned_data = super().clean()
        skill = cleaned_data.get("skill")

        if not self.profile:
            raise forms.ValidationError("Perfil não definido no formulário.")

        if ProfileSkill.objects.filter(
            profile=self.profile,
            skill=skill
        ).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError(
                "Essa habilidade já está cadastrada para este perfil."
            )

        return cleaned_data


class ProfileSkillDetailForm(forms.ModelForm):
    """ Formulário somente leitura para o DetailView """
    class Meta:
        model = ProfileSkill
        fields = [
            "skill",
            "level",
            "notes",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Desabilita todos os campos
        for field in self.fields.values():
            field.disabled = True


class ProfileSystemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.profile = kwargs.pop("profile", None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = ProfileSystem
        fields = [
            "system",
            "level",
            "notes"
        ]

    def clean(self):
        cleaned_data = super().clean()
        system = cleaned_data.get("system")

        if not self.profile:
            raise forms.ValidationError("Perfil não definido no formulário.")

        if ProfileSystem.objects.filter(
            profile=self.profile,
            system=system
        ).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError(
                "Este sistema já está cadastrado para este perfil."
            )

        return cleaned_data


class ProfileSystemDetailForm(forms.ModelForm):
    class Meta:
        model = ProfileSystem
        fields = ["system", "level", "notes"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs["readonly"] = True   # impede edição visual
            field.widget.attrs["disabled"] = True   # impede submissão
