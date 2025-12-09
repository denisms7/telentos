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


class Skill(models.Model):
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


class Talent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=150)
    department = models.CharField(max_length=150, blank=True, null=True)

    skills = models.ManyToManyField(
        Skill,
        through="TalentSkill",
        related_name="talents",
        blank=True,
    )

    certifications = models.ManyToManyField(
        "Certification",
        related_name="talents",
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class TalentSkill(models.Model):
    talent = models.ForeignKey(Talent, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    level = models.CharField(
        max_length=20,
        choices=SkillLevel.choices,
        default=SkillLevel.BASIC,
    )

    class Meta:
        unique_together = ("talent", "skill")
        verbose_name = "Habilidade do Servidor"
        verbose_name_plural = "Habilidades do Servidor"

    def __str__(self):
        return f"{self.talent} - {self.skill} ({self.get_level_display()})"


class Certification(models.Model):
    name = models.CharField("Nome da Certificação", max_length=200)
    institution = models.CharField("Instituição", max_length=200)
    issue_date = models.DateField("Data de Emissão")
    expiration_date = models.DateField("Validade", null=True, blank=True)

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

    def __str__(self):
        return self.name
