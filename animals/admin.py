from django.contrib import admin
from animals.models import Animals, ImagePets, TypeAnimals, Gender, Breed, AgeAnimals

admin.site.register(ImagePets)


@admin.register(Animals)
class AnimalsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'breed', 'type', 'age', 'time_create', 'time_update')
    list_display_links = ('id', 'age', 'name')
    ordering = ['id']


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('id', 'gender_title')
    list_display_links = ('id', 'gender_title')
    ordering = ['id']


@admin.register(TypeAnimals)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_title')
    list_display_links = ('id', 'type_title')
    ordering = ['id']


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ('id', 'breed_title')
    list_display_links = ('id', 'breed_title')
    ordering = ['id']


@admin.register(AgeAnimals)
class AgeAdmin(admin.ModelAdmin):
    list_display = ('id', 'age_title', 'min_age', 'max_age')
    list_display_links = ('id', 'age_title', 'min_age', 'max_age')
    ordering = ['id']


# @admin.register(ImagePets)
# class ImageAdmin(admin.ModelAdmin):
#     list_display = ('id', 'pet', 'image')
#     list_display_links = ('id',)
#     ordering = ['id']
