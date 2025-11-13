from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # Пример дополнительного поля
    middle_name = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.username
