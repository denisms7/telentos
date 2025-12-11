from django.contrib.auth.models import User
from django.db import models
from skills.models import Skill, SkillLevel


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
    position = models.CharField(verbose_name="Cargo", max_length=150, blank=True,)
    registration = models.CharField(verbose_name="Matrícula", max_length=10, blank=True, unique=True,)
    admission_date = models.DateField(verbose_name="Admissão", blank=True, null=True,)

    def __str__(self):
        full_name = self.user.get_full_name().strip()
        return full_name or self.user.username


class Certification(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="certifications",
        verbose_name="Perfil",
    )

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

    workload = models.PositiveIntegerField(
        "Carga Horária (horas)",
        null=True,
        blank=True,
    )

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
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="skills",
    )
    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        related_name="profiles",
    )
    level = models.CharField(
        max_length=20,
        choices=SkillLevel.choices,
    )
    years_experience = models.PositiveSmallIntegerField(default=0)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ("profile", "skill")
        ordering = ("order",)

    def __str__(self):
        return f"{self.skill} - {self.get_level_display()}"
