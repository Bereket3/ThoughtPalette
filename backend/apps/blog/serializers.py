from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField

from .models import BlogComponent, BlogTree


class BlogComponentSerializer(serializers.ModelSerializer):
    next_node = serializers.SerializerMethodField()

    class Meta:
        model = BlogComponent
        fields = [
            "id",
            "content_type",
            "file_content",
            "text_content",
            "next_node",
            "created_at",
            "updated_at",
        ]

    def get_next_node(self, obj):
        if obj.next_node:
            return BlogComponentSerializer(obj.next_node).data
        return None


class BlogTreeSerializer(TaggitSerializer, serializers.ModelSerializer):

    blog_tags = TagListSerializerField()

    class Meta:
        model = BlogTree
        fields = [
            "id",
            "blog_title",
            "blog_owner",
            "blog_tags",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["blog_owner"]

    def validate(self, attrs):
        attrs["blog_owner"] = self.context.get("user")
        return super().validate(attrs)
