"""Forms configuration for messaging app.
"""

from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    """Form to provide contact to admin."""
    class Meta:
        model = Contact
        fields = [
            'sender_name', 'sender_email', 'message',
        ]
