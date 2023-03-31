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
        fields = '__all__'


# Serializer for Staff model
class StaffSerializer(serializers.ModelSerializer):
    job = JobSerializer()
    is_staff = serializers.BooleanField()

    class Meta:
        model = StaffModel
        fields = ['picture', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'job',
                  'instagram_url', 'facebook_url', 'twitter_url']


# Serializer for FAQ model
class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQModel
        fields = "__all__"


# Serializer for Service model
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceModel
        fields = "__all__"


# Serializer for Contact model
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = "__all__"

    def create(self, validated_data):
        return ContactModel.objects.create(**validated_data)


# Serializer for Testimonial model
class TestimonialSerializer(serializers.ModelSerializer):
    client_job = JobSerializer()

    class Meta:
        model = TestimonialModel
        fields = "__all__"


# Serializer for CaseStudy model
class CaseStudySerializer(serializers.ModelSerializer):
    service = ServiceSerializer()

    class Meta:
        model = CaseStudyModel
        fields = "__all__"


# Serializer for Category model
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = "__all__"


# Serializer for Blog model
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = "__all__"
