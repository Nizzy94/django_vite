from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(blank=False, null=False, max_length=200)
    email = models.EmailField(blank=False, null=False)
    subject = models.CharField(blank=False, null=False, max_length=200)
    message = models.TextField(
        blank=False, null=False, max_length=500)

    class Meta():
        verbose_name_plural = 'ContactMessages'
