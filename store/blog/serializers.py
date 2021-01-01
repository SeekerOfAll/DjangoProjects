from django.contrib.auth import get_user_model
from rest_framework import serializers
from account.serializers import UserSerializer
from .models import Post, Category, Comment

User = get_user_model()


class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=128)
    slug = serializers.SlugField()
    content = serializers.CharField()
    create_at = serializers.DateTimeField(read_only=True)
    update_at = serializers.DateTimeField(read_only=True)
    publish_time = serializers.DateTimeField(read_only=True)
    draft = serializers.BooleanField()
    image = serializers.ImageField()
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    def create(self, validated_data):
        """
        Create and return a new `Post` instance, given the validated data.
        """
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.content = validated_data.get('content', instance.content)
        instance.create_at = validated_data.get('create_at', instance.create_at)
        instance.update_at = validated_data.get('update_at', instance.update_at)
        instance.publish_time = validated_data.get('publish_time', instance.publish_time)
        instance.draft = validated_data.get('draft', instance.draft)
        instance.image = validated_data.get('image', instance.image)
        instance.category = validated_data.get('category', instance.category)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        return instance


# class CommentSerializer(serializers.Serializer):
#     content = serializers.CharField()
#     create_at = serializers.DateTimeField(read_only=True)
#     update_at = serializers.DateTimeField(read_only=True)
#     post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
#     author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
#     is_confirmed = serializers.BooleanField()
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Comment` instance, given the validated data.
#         """
#         return Comment.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.content = validated_data.get('content', instance.content)
#         instance.create_at = validated_data.get('create_at', instance.create_at)
#         instance.update_at = validated_data.get('update_at', instance.update_at)
#         instance.post = validated_data.get('post', instance.post)
#         instance.author = validated_data.get('author', instance.author)
#         instance.is_confirmed = validated_data.get('is_confirmed', instance.is_confirmed)
#
#         instance.save()
#         return instance

class CommentSerializer(serializers.ModelSerializer):
    author_detail = UserSerializer(source='author', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
