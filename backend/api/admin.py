from django.contrib import admin
from .models import JobModel, StaffModel, FAQModel, ServiceModel, ContactModel, TestimonialModel, CaseStudyModel, \
    CategoryModel, BlogModel


@admin.register(StaffModel)
class StaffModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name']
    list_display_links = ['username', 'first_name', 'last_name']


admin.site.register(JobModel)
admin.site.register(FAQModel)
admin.site.register(ServiceModel)
admin.site.register(ContactModel)
admin.site.register(TestimonialModel)
admin.site.register(CaseStudyModel)
admin.site.register(CategoryModel)
admin.site.register(BlogModel)
