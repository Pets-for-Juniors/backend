from rest_framework import serializers
from .models import Animals, ImagePets, TypeAnimals


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
#
#
# class SexFilterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Animals
#         fields = ['sex']
#
#
# class BreedFilterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Animals
#         fields = ['type', 'breed']
#
#
# class AgeFilterSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     minAge = serializers.IntegerField()
#     maxAge = serializers.IntegerField()