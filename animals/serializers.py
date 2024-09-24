from rest_framework import serializers
from .models import Animals, ImagePets, TypeAnimals, AgeAnimals, Gender, Breed


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagePets
        fields = ['image']


class AnimalSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Animals
        fields = '__all__'

    def get_images(self, obj):
        queryset = ImagePets.objects.filter(pet=obj)
        return [ImageSerializer(q).data['image'] for q in queryset]


class AnimalListSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Animals
        fields = ['id', 'type', 'gender', 'age', 'breed', 'images']

    def get_images(self, obj):
        queryset = ImagePets.objects.filter(pet=obj).first()
        return ImageSerializer(queryset).data['image']


class TypeFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeAnimals
        fields = ['id', 'type_title']


class AgeFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeAnimals
        fields = '__all__'


class GenderFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'


class BreedFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'
