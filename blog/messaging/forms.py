from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = [
            'sender_name', 'sender_email', 'message',
        ]
