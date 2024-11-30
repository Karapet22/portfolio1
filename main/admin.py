from django.contrib import admin
from .models import (
    Contacts, Services, ServiceType, ContactUs, Projects, ProjectType, Head, AboutUs
)


@admin.register(Head)
class HeadModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'text']
    list_display_links = ['title','text']

@admin.register(Contacts)
class ContactsModelAdmin(admin.ModelAdmin):
    list_display = ['phone', 'email', 'address']
    list_display_links = ['phone', 'email', 'address']

@admin.register(Services)
class ServicesModelAdmin(admin.ModelAdmin):
    list_display=['title','text']
    list_display_links=['title','text']

@admin.register(ServiceType)
class ServicesModelAdmin(admin.ModelAdmin):
    list_display=['title']
    list_display_links=['title']


@admin.register(ContactUs)
class ContactUsModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'email', 'subject']
    list_display_links = ['name', 'surname', 'email', 'subject']
    
@admin.register(Projects)
class ProjectsModelAdmin(admin.ModelAdmin):
    list_display = ['title','text']
    list_display_links = ['title', 'text']

@admin.register(ProjectType)
class ProjectTypeModelAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']

    
@admin.register(AboutUs)
class AboutUsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'marketing_percentage', 'digital_media', 'social_media_maneging']
    list_display_links = ['id', 'title', 'marketing_percentage', 'digital_media', 'social_media_maneging']