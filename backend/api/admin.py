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
@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ["company", "email", "subject", "created_at"]
    list_display_links = ["company", "email"]
    readonly_fields = ["full_name", "company", "email", "subject", "message", "created_at"]
    ordering = ["-created_at"]
admin.site.register(TestimonialModel)
admin.site.register(CaseStudyModel)
admin.site.register(CategoryModel)
admin.site.register(BlogModel)
