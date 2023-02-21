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
    class Meta:
        model = JobModel
        fields = ['id', 'job']

    # Method for creation
    def create(self, validated_data):
        job = JobModel(**validated_data)
        job.save()
        return job



# Serializer for Staff model
class StaffSerializer(serializers.ModelSerializer):
    # job = JobSerializer(read_only=True)
    class Meta:
        model = StaffModel
        fields = ['picture', 'username', 'first_name', 'last_name', 'email', 'password', 'is_staff',
                  'instagram_url', 'facebook_url', 'twitter_url']

    def create(self, validated_data):
        staff = StaffModel(**validated_data)
        staff.set_password(validated_data['password'])
        staff.save()
        return staff


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
