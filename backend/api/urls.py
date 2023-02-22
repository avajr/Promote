from django.urls import path
from .views import JobAPIView, \
    StaffAPIView, \
    FAQAPIView, \
    ServiceAPIView, \
    ContactAPIView, \
    TestimonialAPIView, \
    CaseStudyAPIView, \
    CategoryAPIView, \
    BlogAPIView

urlpatterns = [
    path('jobs/', JobAPIView.as_view()),
    path('staff/', StaffAPIView.as_view()),
    path('faqs/', FAQAPIView.as_view()),
    path('services/', ServiceAPIView.as_view()),
    path('contacts/', ContactAPIView.as_view()),
    path('testimonials/', TestimonialAPIView.as_view()),
    path('case-studies/', CaseStudyAPIView.as_view()),
    path('categories/', CategoryAPIView.as_view()),
    path('blogs/', BlogAPIView.as_view())
]