from rest_framework import serializers
from .models import JobModel, \
    StaffModel, \
    FAQModel, \
    ServiceModel, \
    ContactModel, \
    TestimonialModel, \
    CaseStudyModel, \
    CategoryModel, \
    BlogModel


# Serializer for Job model
class JobSerializer(serializers.ModelSerializer):
    pass


# Serializer for Staff model
class StaffSerializer(serializers.ModelSerializer):
    pass


# Serializer for FAQ model
class FAQSerializer(serializers.ModelSerializer):
    pass


# Serializer for Service model
class ServiceSerializer(serializers.ModelSerializer):
    pass


# Serializer for Contact model
class ContactSerializer(serializers.ModelSerializer):
    pass


# Serializer for Testimonial model
class TestimonialSerializer(serializers.ModelSerializer):
    pass


# Serializer for CaseStudy model
class CaseStudySerializer(serializers.ModelSerializer):
    pass


# Serializer for Category model
class CategorySerializer(serializers.ModelSerializer):
    pass


# Serializer for Blog model
class BlogSerializer(serializers.ModelSerializer):
    pass
