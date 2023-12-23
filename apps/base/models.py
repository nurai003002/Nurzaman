from django.db import models
from ckeditor.fields import RichTextField
from apps.secondary.models import Kvartal

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название'
    )
    descriptions = models.TextField(
        verbose_name = 'Описание'
    )
    phone = models.CharField(
        max_length = 255,
        verbose_name = 'Телефон'
    )
    email = models.EmailField(
        verbose_name = 'Почта'
    )  
    logo_complex = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип'
    )
    location = models.CharField(
        max_length = 255,
        verbose_name = 'Адрес'
    )
    whatsapp = models.CharField(
        max_length = 255,
        verbose_name = 'whatsapp URL',
        blank=True, null=True
    )
    instagram = models.CharField(
        max_length = 255,
        verbose_name = 'instagram URL',
        blank=True, null=True
    )
    facebook = models.CharField(
        max_length = 255,
        verbose_name = 'facebook URL',
        blank=True, null=True
    )
    box_office = RichTextField(
        verbose_name = 'Офис продажи'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = "Настройки"


class SettingsPhone(models.Model):
    settings = models.ForeignKey(Settings, related_name='phone_title' , on_delete=models.CASCADE)
    phone = models.CharField(
        max_length = 255,
        verbose_name = 'Телефонный номер'
    )
    class Meta:
        unique_together = ('settings', 'phone')

class About(models.Model):
    image = models.ImageField(
        upload_to='about_image',
        verbose_name='Фотография'
    )
    descriptions = RichTextField(
        verbose_name = 'Информационный текст',
        blank =True, null = True
    )
    def __str__(self):
        return self.descriptions
    
    class Meta:
        verbose_name = 'O нас'
        verbose_name_plural = "О нас"



class SettingsPlace(models.Model):
    kvartal = models.ForeignKey(Kvartal, related_name='place_kvartal' , on_delete=models.CASCADE)
    place = models.CharField(
        max_length = 255,
        verbose_name = 'Места в комплексе'
    )
    class Meta:
        unique_together = ('kvartal', 'place')
        




