from rest_framework import serializers

from .models import Article, Author, Comment

class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()
    body = serializers.CharField()
    author = serializers.CharField()

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.body = validated_data.get('body', instance.body)
        instance.author = validated_data.get('author', instance.author_id)

        instance.save()
        return instance

class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        if Author.objects.filter(name = validated_data["name"]).exists():
            raise Exception('User already exists')
        return Author.objects.create(**validated_data)

class CommentSerializer(serializers.Serializer):
    body = serializers.CharField()
    author = serializers.CharField()
    assigned = serializers.IntegerField()

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)
    