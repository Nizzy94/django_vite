from django.utils import timezone
from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(blank=False, null=False, max_length=40)
    email = models.EmailField(blank=False, null=False)
    subject = models.CharField(blank=False, null=False, max_length=200)
    message = models.TextField(
        blank=False, null=False, max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta():
        verbose_name_plural = 'ContactMessages'

    def save(self, *args, **kwargs) -> None:
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)


class SocialIcon(models.Model):
    provider = models.CharField(blank=False, null=False, max_length=40)
    icon = models.URLField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta():
        verbose_name_plural = 'SocialIcons'

    def save(self, *args, **kwargs) -> None:
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)
