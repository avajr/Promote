from rest_framework import serializers

from blog.models import CaseStudy, Blog, Category
from common.serializers import ServiceSerializer



# Serializer for CaseStudy model
class CaseStudySerializer(serializers.ModelSerializer):
    service = ServiceSerializer()

    class Meta:
        model = CaseStudy
        fields = "__all__"


# Serializer for Category model
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


# Serializer for Blog model
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"
