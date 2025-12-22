from django.contrib.auth.models import User
from django.db import models
from skills.models import Skill, SkillLevel, System, Function


class CertificationType(models.TextChoices):
    TECHNICAL = "technical", "Curso Técnico"

    GRADUATION = "graduation", "Graduação"
    POSTGRADUATION = "postgraduation", "Pós-graduação"
    MBA = "mba", "MBA"

    MASTER = "master", "Mestrado"
    DOCTORATE = "doctorate", "Doutorado"
    POSTDOCTORATE = "postdoctorate", "Pós-doutorado"

    COURSE = "course", "Curso"
    TRAINING = "training", "Treinamento"
    WORKSHOP = "workshop-Oficina", "Workshop/Oficina"


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name="Usuário", on_delete=models.CASCADE, related_name="profile", unique=True,)
    registration = models.CharField(verbose_name="Matrícula", max_length=10, blank=True, null=True,)
    function = models.ForeignKey(Function, verbose_name="Cargo Efetivo", on_delete=models.PROTECT, related_name="Function", blank=True, null=True,)
    admission_date = models.DateField(verbose_name="Admissão", blank=True, null=True,)
    cpf = models.CharField(max_length=14, verbose_name="CPF", unique=True)
    phrase = models.CharField(max_length=250, verbose_name="Frase de Perfil", blank=True, null=True,)
    public = models.BooleanField(verbose_name="Perfil Público", default=True)

    def __str__(self):
        full_name = self.user.get_full_name().strip()
        return full_name or self.user.username

    @property
    def course_count(self):
        return self.certifications.filter(
            certification_type__in=[
                CertificationType.COURSE,
                CertificationType.TRAINING,
                CertificationType.WORKSHOP,
            ]
        ).count()

    @property
    def technical_count(self):
        return self.certifications.filter(
            certification_type=CertificationType.TECHNICAL
        ).count()

    @property
    def graduations_count(self):
        return self.certifications.filter(
            certification_type=CertificationType.GRADUATION
        ).count()

    @property
    def postgraduations_count(self):
        return self.certifications.filter(
            certification_type__in=[
                CertificationType.POSTGRADUATION,
                CertificationType.MBA,
            ]
        ).count()

    @property
    def masters_doctorates_count(self):
        return self.certifications.filter(
            certification_type__in=[
                CertificationType.MASTER,
                CertificationType.DOCTORATE,
                CertificationType.POSTDOCTORATE,
            ]
        ).count()


class Certification(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="certifications", verbose_name="Perfil",)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Cadastro")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Alteração")

    certification_type = models.CharField(
        "Tipo de Certificação",
        max_length=20,
        choices=CertificationType.choices,
        default=CertificationType.COURSE,
    )

    name = models.CharField("Nome da Certificação", max_length=200)
    institution = models.CharField("Instituição", max_length=200)
    workload = models.PositiveIntegerField("Carga Horária", null=True, blank=True,)
    issue_date = models.DateField("Data de Emissão")

    file = models.FileField(
        "Arquivo (PDF)",
        upload_to="certifications/%Y/%m/",
        null=True,
        blank=True,
    )

    link = models.URLField(
        "Link do Certificado",
        max_length=500,
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ("-issue_date",)
        verbose_name = "Certificado"
        verbose_name_plural = "Certificados"

    def __str__(self):
        return self.name


class ProfileSkill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="skills",)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Cadastro")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Alteração")

    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name="profiles", verbose_name="Habilidade",)
    level = models.IntegerField(choices=SkillLevel.choices, verbose_name="Nível", default=SkillLevel.ROBOTIC)
    notes = models.TextField("Observações", blank=True,)

    class Meta:
        unique_together = ("profile", "skill")
        verbose_name = "Habilidade do Perfil"
        verbose_name_plural = "Habilidades por Perfil"
        ordering = ("-level", "skill")

    def __str__(self):
        return f"{self.skill} - {self.get_level_display()}"


class ProfileSystem(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="systems", verbose_name="Perfil",)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Cadastro")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Alteração")

    system = models.ForeignKey(System, on_delete=models.CASCADE, related_name="profiles", verbose_name="Sistema",)
    level = models.IntegerField(choices=SkillLevel.choices, verbose_name="Nível", default=SkillLevel.ROBOTIC)
    notes = models.TextField("Observações", blank=True,)

    class Meta:
        unique_together = ("profile", "system")
        verbose_name = "Sistema do Perfil"
        verbose_name_plural = "Sistemas por Perfil"
        ordering = ("-level", "system")

    def __str__(self):
        return f"{self.system} - {self.get_level_display()}"
