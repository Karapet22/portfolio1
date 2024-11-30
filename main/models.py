from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Head(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    
    class Meta:
        verbose_name = "Head"
        verbose_name_plural = 'Head'
        
 
class Contacts(models.Model):
    phone = PhoneNumberField()
    email = models.EmailField()
    address = models.CharField(max_length=255)

    facebook = models.URLField()
    twitter = models.URLField()
    linkedin = models.URLField()
    gmail = models.URLField()



    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
        
class Services(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

class ServiceType(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="media/ServiceImages")
    
    class Meta:
        verbose_name = 'ServiceType'
        verbose_name_plural = 'ServiceTypes'



class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'


class Projects(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        
class ProjectType(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to= 'media/ProjectImages')
    
    class Meta:
        verbose_name = 'ProjectType'
        verbose_name_plural = 'ProjectTypes'


class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    
    marketing_percentage = models.DecimalField(max_digits=2, decimal_places=0, )
    digital_media = models.DecimalField(max_digits=2, decimal_places=0, null= True)
    social_media_maneging = models.DecimalField(max_digits=2, decimal_places=0, null= True)
    
    text2 = models.TextField(null= True)
    
    # def save(self, force_insert = ..., force_update = ..., using = ..., update_fields = ...):
        # self.marketing_percentage = round(self.marketing_percentage)
        # return super().save(force_insert, force_update, using, update_fields)
    
    class Meta:
        verbose_name = 'AboutUs'
        verbose_name_plural = 'AboutUs'
        
        