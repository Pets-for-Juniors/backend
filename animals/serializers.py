from rest_framework import serializers
from .models import Animals, ImagePets


class ImageSerialiser(serializers.ModelSerializer):
    class Meta:
        model = ImagePets
        fields = ['image']


class AnimalSerialiser(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Animals
        fields = '__all__'

    def get_images(self, obj):
        queryset = ImagePets.objects.filter(pet=obj)
        return [ImageSerialiser(q).data['image'] for q in queryset]
