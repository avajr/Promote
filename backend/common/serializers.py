from rest_framework import serializers

from common.models import FAQ, Service, Contact, Testimonial
from users.api.serializers import JobSerializer


# Serializer for FAQ model
class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = "__all__"


# Serializer for Service model
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


# Serializer for Contact model
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

    def create(self, validated_data):
        return Contact.objects.create(**validated_data)


# Serializer for Testimonial model
class TestimonialSerializer(serializers.ModelSerializer):
    client_job = JobSerializer()

    class Meta:
        model = Testimonial
        fields = "__all__"
