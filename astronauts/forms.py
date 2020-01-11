from django import forms

from astronauts.models import Astronaut


class AstronautForm(forms.ModelForm):
    class Meta:
        model = Astronaut
        fields = ['first_name', 'last_name', 'date_of_birth']
