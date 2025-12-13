from django.db import models
from ckeditor.fields import RichTextField


class SkillLevel(models.IntegerChoices):
    ROBOTIC = 0, "Robótico"
    BASIC = 1, "Básico"
    INTERMEDIATE = 2, "Intermediário"
    ADVANCED = 3, "Avançado"
    EXPERT = 4, "Especialista"


class SkillType(models.TextChoices):
    HARD = "hard", "Hard Skill"
    SOFT = "soft", "Soft Skill"


class Skill(models.Model):
    created_at = models.DateTimeField("Criação", auto_now_add=True)
    active = models.BooleanField("Ativo", default=True,)
    name = models.CharField(max_length=100)
    skill_type = models.CharField(max_length=10, choices=SkillType.choices,)

    class Meta:
        unique_together = ("name", "skill_type")
        verbose_name = "Habilidade"
        verbose_name_plural = "Habilidades"

    def __str__(self):
        return f"{self.name} ({self.get_skill_type_display()})"


class System(models.Model):
    created_at = models.DateTimeField("Criação", auto_now_add=True)
    active = models.BooleanField("Ativo", default=True,)
    name = models.CharField("Nome do Sistema", max_length=150, unique=True,)
    description = models.TextField("Descrição", blank=True,)

    class Meta:
        verbose_name = "Sistema"
        verbose_name_plural = "Sistemas"
        ordering = ("name",)

    def __str__(self):
        return f"{self.name}"


class Function(models.Model):
    created_at = models.DateTimeField("Criação", auto_now_add=True)
    active = models.BooleanField("Ativo", default=True,)
    name = models.CharField(max_length=100, verbose_name='Nome do Cargo')
    description = RichTextField(max_length=10000, verbose_name='Atribuições Basicas')

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"

    def __str__(self):
        return f"{self.name}"
