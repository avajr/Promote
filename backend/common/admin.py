from django.contrib import admin

from common.models import FAQ, Service, Contact, Testimonial


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer')
    list_display_links = ('id', 'question', 'answer')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'company', 'email', 'subject')
    list_display_links = ('id', 'full_name', 'company', 'email', 'subject')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_full_name', 'feedback', 'company')
    list_display_links = ('id', 'client_full_name', 'feedback', 'company')

