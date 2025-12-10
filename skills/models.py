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
