from django.contrib.auth.models import User
from django.db import models


class SkillNivel(models.TextChoices):
    BASICO = "basico", "Básico"
    INTERMEDIARIO = "intermediario", "Intermediário"
    AVANCADO = "avancado", "Avançado"
    ESPECIALISTA = "especialista", "Especialista"


class SkillType(models.TextChoices):
    HARD = "hard", "Hard Skill"
    SOFT = "soft", "Soft Skill"


class Categoria(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name


class Skill(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(
        max_length=10,
        choices=SkillTipo.choices
    )

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
        unique_together = ('nome', 'tipo')

    def __str__(self):
        return f"{self.nome} ({self.get_tipo_display()})"


class Talento(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    cargo = models.CharField(max_length=150)
    setor = models.CharField(max_length=150, blank=True, null=True)

    categorias = models.ManyToManyField(Categoria, blank=True)
    skills = models.ManyToManyField("Skill", through="TalentoSkill", blank=True)

    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class TalentoSkill(models.Model):
    talento = models.ForeignKey(Talento, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    nivel = models.CharField(
        max_length=20,
        choices=SkillNivel.choices,
        default=SkillNivel.BASICO
    )

    class Meta:
        unique_together = ('talento', 'skill')

    def __str__(self):
        return f"{self.talento} - {self.skill} ({self.get_nivel_display()})"
