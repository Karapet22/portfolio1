from django.forms import ModelForm
from .models import ContactUs

class ContactForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = "__all__"
        
        # fields = ['name', 'email'....]