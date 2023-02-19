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
class JobModel(serializers.ModelSerializer):
    pass


# Serializer for Staff model
class StaffModel(serializers.ModelSerializer):
    pass


# Serializer for FAQ model
class FAQModel(serializers.ModelSerializer):
    pass


# Serializer for Service model
class ServiceModel(serializers.ModelSerializer):
    pass


# Serializer for Contact model
class ContactModel(serializers.ModelSerializer):
    pass


# Serializer for Testimonial model
class TestimonialModel(serializers.ModelSerializer):
    pass


# Serializer for CaseStudy model
class CaseStudyModel(serializers.ModelSerializer):
    pass


# Serializer for Category model
class CategoryModel(serializers.ModelSerializer):
    pass


# Serializer for Blog model
class BlogModel(serializers.ModelSerializer):
    pass
