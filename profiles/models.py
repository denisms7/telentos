from django.contrib.auth.models import User
from django.db import models
from certifications.models import Skill, Certification, SkillLevel


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    sector = models.CharField(
        max_length=150,
        blank=True,
    )

    def __str__(self):
        return self.user.get_full_name() or self.user.username


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

    class Meta:
        unique_together = ("profile", "skill")

    def __str__(self):
        return f"{self.skill} - {self.get_level_display()}"


class ProfileCertification(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="certifications",
    )
    certification = models.ForeignKey(
        Certification,
        on_delete=models.CASCADE,
        related_name="profiles",
    )

    class Meta:
        unique_together = ("profile", "certification")

    def __str__(self):
        return str(self.certification)
