from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView

from common import serializers, models


class FAQAPIView(ListAPIView):
    serializer_class = serializers.FAQSerializer
    queryset = models.FAQ.objects.all()


class ServiceAPIView(ListAPIView):
    serializer_class = serializers.ServiceSerializer
    queryset = models.Service.objects.all()


class ContactAPIView(ListCreateAPIView):
    serializer_class = serializers.ContactSerializer
    queryset = models.Contact.objects.all()


class TestimonialAPIView(ListAPIView):
    serializer_class = serializers.TestimonialSerializer
    queryset = models.Testimonial.objects.all()

