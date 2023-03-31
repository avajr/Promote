from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView
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


class JobAPIView(ListAPIView):
    serializer_class = JobSerializer
    queryset = JobModel.objects.all()


class StaffAPIView(ListAPIView):
    serializer_class = StaffSerializer
    queryset = StaffModel.objects.all()


class FAQAPIView(ListAPIView):
    serializer_class = FAQSerializer
    queryset = FAQModel.objects.all()


class ServiceAPIView(ListAPIView):
    serializer_class = ServiceSerializer
    queryset = ServiceModel.objects.all()


class ContactAPIView(ListCreateAPIView):
    serializer_class = ContactSerializer
    queryset = ContactModel.objects.all()


class TestimonialAPIView(ListAPIView):
    serializer_class = TestimonialSerializer
    queryset = TestimonialModel.objects.all()


class CaseStudyAPIView(ListAPIView):
    serializer_class = CaseStudySerializer
    queryset = CaseStudyModel.objects.all()

class CaseStudyRetrieveAPIView(RetrieveAPIView):
    serializer_class = CaseStudySerializer
    queryset = CaseStudyModel.objects.all()

class CategoryAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = CategoryModel.objects.all()


class BlogAPIView(ListAPIView):
    serializer_class = BlogSerializer
    queryset = BlogModel.objects.all()

class BlogRetrieveAPIView(RetrieveAPIView):
    serializer_class = BlogSerializer
    queryset = BlogModel.objects.all()