from django.contrib.auth.models import User
from django.db import models


class SkillLevel(models.TextChoices):
    BASIC = "basic", "Básico"
    INTERMEDIATE = "intermediate", "Intermediário"
    ADVANCED = "advanced", "Avançado"
    EXPERT = "expert", "Especialista"


class SkillType(models.TextChoices):
    HARD = "hard", "Hard Skill"
    SOFT = "soft", "Soft Skill"


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


class Skill(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    skill_type = models.CharField(
        max_length=10,
        choices=SkillType.choices,
    )

    class Meta:
        unique_together = ("name", "skill_type")
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return f"{self.name} ({self.get_skill_type_display()})"


class Certification(models.Model):
    created_at = models.DateTimeField(
        "Data de Cadastro",
        auto_now_add=True,
    )

    certification_type = models.CharField(
        "Tipo de Certificação",
        max_length=20,
        choices=CertificationType.choices,
        default=CertificationType.COURSE,
    )

    name = models.CharField(
        "Nome da Certificação",
        max_length=200,
    )
    institution = models.CharField(
        "Instituição",
        max_length=200,
    )

    workload = models.PositiveIntegerField(
            "Carga Horária (horas)",
            help_text="Informe a carga horária total em horas.",
            null=True,
            blank=True,
        )

    issue_date = models.DateField(
        "Data de Emissão",
    )

    skills = models.ManyToManyField(
        Skill,
        related_name="certifications",
        blank=True,
    )

    file = models.FileField(
        "Arquivo (PDF)",
        upload_to="certifications/",
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
        verbose_name = "Certificação"
        verbose_name_plural = "Certificações"
        ordering = ("-issue_date",)

    def __str__(self):
        return f"{self.name} ({self.get_certification_type_display()})"


class System(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(
        "Ativo",
        default=True,
    )
    name = models.CharField(
        "Nome do Sistema",
        max_length=150,
        unique=True,
    )
    description = models.TextField(
        "Descrição",
        blank=True,
    )
    owner_sector = models.CharField(
        "Setor Responsável",
        max_length=150,
        blank=True,
    )

    class Meta:
        verbose_name = "Sistema"
        verbose_name_plural = "Sistemas"
        ordering = ("name",)

    def __str__(self):
        return f"{self.name}"
