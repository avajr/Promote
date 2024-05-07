from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework import filters

from blog import serializers, models


class CaseStudyAPIView(ListAPIView):
    serializer_class = serializers.CaseStudySerializer
    queryset = models.CaseStudy.objects.all()


class CaseStudyRetrieveAPIView(RetrieveAPIView):
    serializer_class = serializers.CaseStudySerializer
    queryset = models.CaseStudy.objects.all()


class CategoryAPIView(ListAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()


class BlogAPIView(ListAPIView):
    serializer_class = serializers.BlogSerializer
    queryset = models.Blog.objects.all().order_by('?')

    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)

    search_fields = ('title', 'short_description',)
    ordering_fields = ('updated_at',)


class BlogRetrieveAPIView(RetrieveAPIView):
    serializer_class = serializers.BlogSerializer
    queryset = models.Blog.objects.all()
