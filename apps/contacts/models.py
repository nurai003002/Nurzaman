from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Имя'
    )
    email = models.EmailField(
        verbose_name = 'Почта'
    )
    number = models.CharField(
        max_length = 255,
        verbose_name = 'Номер телефона'
    )
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Запрос на связь'
        verbose_name_plural = 'Запросы на связь'