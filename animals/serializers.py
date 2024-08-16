from rest_framework import serializers
from .models import Animals, ImagePets


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
        fields = ['id', 'type', 'sex', 'age', 'breed', 'images']

    def get_images(self, obj):
        queryset = ImagePets.objects.filter(pet=obj).first()
        return ImageSerializer(queryset).data['image']


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animals
        fields = ['breed', 'type']


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animals
        fields = ['type']


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animals
        fields = ['sex']


class AgeSerializer(serializers.Serializer):
    title = serializers.CharField()
    minAge = serializers.IntegerField()
    maxAge = serializers.IntegerField()

