from django.db import models


# Create your models here.

class Animals(models.Model):
    type = [
        ('dog', 'dog'),
        ('cat', 'cat'),
    ]

    sex = [
        ('male', 'male'),
        ('female', 'female'),
    ]

    type = models.CharField(max_length=100, choices=type, blank=False, verbose_name='Вид')
    name = models.CharField(max_length=200, blank=False, verbose_name='Имя')
    sex = models.CharField(max_length=100, blank=False, choices=sex, verbose_name='Пол')
    breed = models.CharField(max_length=200, blank=False, verbose_name='Порода')
    age = models.PositiveSmallIntegerField(blank=False, verbose_name='Возраст')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Животные'
        verbose_name = 'Животное'
        verbose_name_plural = 'Животные'


class ImagePets(models.Model):
    pet = models.ForeignKey(Animals, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='PetPics', verbose_name='Изображение', blank=True)

    class Meta:
        db_table = 'Изображения животных'
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
