from .models import Members
from django import forms

class MemberForm(forms.ModelForm):
    class Meta:
        model = Members
        fields = (
            'full_name',
            'member_type',
            'image',
            'email',
            'dob',
            'address',
            'contact_no'
        )
