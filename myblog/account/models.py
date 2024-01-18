from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Account(models.Model):
    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    phone = models.CharField(
        max_length=15
    )

    birthday = models.DateTimeField()
