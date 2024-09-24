from django.db import models


# Create your models here.
class TypeAnimals(models.Model):
    type_title = models.CharField(max_length=200, blank=False, verbose_name='Тип', unique=True)

    class Meta:
        db_table = 'Тип'
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def __str__(self):
        return self.type_title


class Gender(models.Model):
    gender_title = models.CharField(max_length=100, blank=False, verbose_name='Пол')

    class Meta:
        db_table = 'Пол'
        verbose_name = 'Пол'
        verbose_name_plural = 'Пол'

    def __str__(self):
        return self.gender_title


class Breed(models.Model):
    breed_title = models.CharField(max_length=200, blank=False, verbose_name='Порода', unique=True)
    type = models.ForeignKey(TypeAnimals, default=None, related_name='id_type', verbose_name='Тип',
                             on_delete=models.CASCADE)

    class Meta:
        db_table = 'Порода'
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'

    def __str__(self):
        return self.breed_title


class Animals(models.Model):
    type = models.ForeignKey(TypeAnimals, default=None, related_name='type_pet', verbose_name='Тип',
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=False, verbose_name='Имя')
    gender = models.ForeignKey(Gender, default=None, related_name='gender_pet', verbose_name='Пол',
                               on_delete=models.CASCADE)
    breed = models.ForeignKey(Breed, default=None, related_name='breed_pet', verbose_name='Порода',
                              on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField(blank=False, verbose_name='Возраст')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Животные'
        verbose_name = 'Животное'
        verbose_name_plural = 'Животные'

    def __str__(self):
        return self.name


class ImagePets(models.Model):
    pet = models.ForeignKey(Animals, default=None, related_name='pet', on_delete=models.CASCADE, verbose_name='Питомец')
    image = models.ImageField(upload_to='petpics', verbose_name='Изображение', blank=True)

    class Meta:
        db_table = 'Изображения животных'
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'

    def __str__(self):
        return self.pet


class AgeAnimals(models.Model):
    age_title = models.CharField(max_length=200, blank=True, verbose_name='Категория', unique=True)
    min_age = models.PositiveSmallIntegerField(blank=True, verbose_name='Минимальный возраст')
    max_age = models.PositiveSmallIntegerField(blank=True, verbose_name='Максимальный возраст')

    class Meta:
        db_table = 'Возраст'
        verbose_name = 'Возраст'
        verbose_name_plural = 'Возраст'

    def __str__(self):
        return self.age_title
