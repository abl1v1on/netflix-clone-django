from rest_framework import serializers

from . import models


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=500)
#     desc = serializers.CharField(required=False, allow_blank=True, allow_null=True)
#     date_created = serializers.DateTimeField(read_only=True)
#     uuid = serializers.UUIDField(read_only=True)
#     type = serializers.CharField(max_length=10)
#     video = serializers.FileField()
#     cover = serializers.ImageField()
#     poster = serializers.ImageField()
#     age_limit = serializers.CharField(max_length=10)
#
#     def create(self, validated_data):
#         return models.Movie.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.desc = validated_data.get('desc', instance.desc)
#         instance.date_created = validated_data.get('date_created', instance.date_created)
#         instance.uuid = validated_data.get('uuid', instance.uuid)
#         instance.type = validated_data.get('type', instance.type)
#         instance.video = validated_data.get('video', instance.video)
#         instance.cover = validated_data.get('cover', instance.cover)
#         instance.poster = validated_data.get('poster', instance.poster)
#         instance.age_limit = validated_data.get('age_limit', instance.age_limit)
#         instance.save()
#         return instance


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = '__all__'

