from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from users.api.views import UserViewSet, JobAPIView, StaffAPIView
from common import views as common_views
from blog import views as blog_views


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)


app_name = "api"
urlpatterns = router.urls

urlpatterns += [
    path('jobs/', JobAPIView.as_view()),
    path('staff/', StaffAPIView.as_view()),
    path('faqs/', common_views.FAQAPIView.as_view()),
    path('services/', common_views.ServiceAPIView.as_view()),
    path('contacts/', common_views.ContactAPIView.as_view()),
    path('testimonials/', common_views.TestimonialAPIView.as_view()),
    path('case-studies/', blog_views.CaseStudyAPIView.as_view()),
    path('case-studies/<int:pk>/', blog_views.CaseStudyRetrieveAPIView.as_view()),
    path('categories/', blog_views.CategoryAPIView.as_view()),
    path('blogs/', blog_views.BlogAPIView.as_view()),
    path('blogs/<int:pk>/', blog_views.BlogRetrieveAPIView.as_view()),
]
