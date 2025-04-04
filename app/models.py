from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Уникальное поле для email
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Необязательное поле для номера телефона

    USERNAME_FIELD = 'email'  # Указываем, что уникальным полем будет email
    REQUIRED_FIELDS = []  # Если есть поля, которые должны быть обязательными, укажите их здесь

    def save(self, *args, **kwargs):
        if not self.username:  # Если username пустой
            self.username = self.email  # Присваиваем значение email
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email
