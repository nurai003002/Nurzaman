from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Slide(models.Model):
    image = models.ImageField(
        upload_to='slide_image',
        verbose_name = 'Фотография'
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название'
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'

class Projects(models.Model):
    image = models.ImageField(
        upload_to='Image_partner',
        verbose_name='Фотография'
    )
    
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

class Kvartal(models.Model):
    image = models.ImageField(
        upload_to='image_europe',
        verbose_name="Фотография "
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название'
    )
    descriptions = RichTextField(
        verbose_name = 'Информационный текст',
        blank =True, null = True
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Квартал'
        verbose_name_plural = 'Кварталы'


class Place(models.Model):
    name = RichTextField(
        verbose_name = 'Название'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Месты'


class PlaceInlineInfo(models.Model):
    place_info = models.ForeignKey(Place,related_name = "place_inline_info", on_delete  = models.CASCADE )
    descriptions = RichTextField(
        verbose_name = 'Информационный текст',
        blank =True, null = True
    )
    class Meta:
        unique_together = ('place_info', 'descriptions')
        

class Gallery(models.Model):
    title = RichTextField(
        verbose_name = "Информационный текст",
        blank = True,null  = True
    )
    def __str__(self):
        return self.title    
    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'


class GalleryImage(models.Model):
    place_info = models.ForeignKey(Gallery,related_name = "gallery_image", on_delete  = models.CASCADE )
    image = models.ImageField(
        upload_to="gallery",
        verbose_name="Фотография"
    )
    class Meta:
        unique_together = ('place_info', 'image')


class Main(models.Model):
    title = RichTextField(
        verbose_name = "Информационный текст",
        blank = True,null  = True
    )
    def __str__(self):
        return self.title    
    class Meta:
        verbose_name = 'Примущество'
        verbose_name_plural = 'Примущества'


class MainImage(models.Model):
    place_info = models.ForeignKey(Main,related_name = "main_image", on_delete  = models.CASCADE )
    image = models.ImageField(
        upload_to="main_photo",
        verbose_name="Фотография"
    )
    class Meta:
        unique_together = ('place_info', 'image')



class Main2(models.Model):
    title = RichTextField(
        verbose_name = "Информационный текст",
        blank = True,null  = True
    )
    def __str__(self):
        return self.title    
    class Meta:
        verbose_name = 'Примущество2'
        verbose_name_plural = 'Примущества2'

class MainImage2(models.Model):
    place_info = models.ForeignKey(Main2,related_name = "main2_image", on_delete  = models.CASCADE )
    image = models.ImageField(
        upload_to="main2_photo",
        verbose_name="Фотография"
    )
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Навзание'
    )
    descriptions = models.TextField(
        verbose_name = 'Описание'
    )
    class Meta:
        unique_together = ('place_info', 'image')



class Environment(models.Model):
    image = models.ImageField(
        verbose_name = "Фотография",
        blank = True, null  = True
    )
    title = RichTextField(
        verbose_name = 'Название',
        blank = True, null  = True
    )
      
    class Meta:
        verbose_name = 'Окружение'
        verbose_name_plural = 'Окружении'

class EnvironmentImage(models.Model):
    place_info = models.ForeignKey(Environment,related_name = "school_univers", on_delete  = models.CASCADE )
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Номер школы'
    )
    time = models.CharField(
        max_length = 255,
        verbose_name = 'Время'
    )

    def __str__(self):
        return self.name
    class Meta:
        unique_together = ('place_info', 'name')

class Street(models.Model):
    title = RichTextField(
        verbose_name = 'Название улицы'
    )
    descriptions = RichTextField(
        verbose_name = 'Описание'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы '

class Reach(models.Model):
    name = RichTextField(
        verbose_name = 'Название'
    )
    class Meta:
        verbose_name = 'Гордость'
        verbose_name_plural = 'Гордости'

class ReachText(models.Model):
    place_info = models.ForeignKey(Reach, related_name = "achievement", on_delete  = models.CASCADE )
    text = RichTextField(
        verbose_name = 'Короткое описание'
    )
    class Meta:
        unique_together = ('place_info', 'text')
  
        
class Apartment(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название квартиры'
    )
    image = models.ImageField(
        upload_to='image_apartment',
        verbose_name='Фото_комнаты'
    )
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural ='Квартиры'

class ApartmentPluse(models.Model):
    place_info = models.ForeignKey(Apartment, related_name = "department", on_delete  = models.CASCADE )
    rooms = models.CharField(
        max_length = 255,
        verbose_name = 'Название комнаты'
    )
    meters = models.CharField(
        max_length = 255,
        verbose_name = 'Площадь комнаты'
    )
    class Meta:
        unique_together = ('place_info', 'rooms')


        
    