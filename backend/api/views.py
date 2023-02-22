from rest_framework.generics import ListCreateAPIView
from .serializers import JobSerializer, \
    StaffSerializer, \
    FAQSerializer, \
    ServiceSerializer, \
    ContactSerializer, \
    TestimonialSerializer, \
    CaseStudySerializer, \
    CategorySerializer, \
    BlogSerializer
from .models import JobModel, \
    StaffModel, \
    FAQModel, \
    ServiceModel, \
    ContactModel, \
    TestimonialModel, \
    CaseStudyModel, \
    CategoryModel, \
    BlogModel


class TestAPI(ListCreateAPIView):
    serializer_class = TestimonialSerializer
    queryset = TestimonialModel.objects.all()

