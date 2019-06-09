from .models import Events
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'


class EventAddForm(forms.ModelForm):
    start_date = forms.DateField(widget=DateInput)
    end_date = forms.DateField(widget=DateInput)
    class Meta:
        model = Events
        fields = ('__all__')
        