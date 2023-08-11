from .models import booking,destination
from django import forms  

class booking_form(forms.ModelForm):
    class Meta:
        model=booking 
        fields="__all__"
    def clean(self):
        cleaned_data=self.cleaned_data
        data=cleaned_data.get('Destination_id')
        id=destination.objects.filter(destination_id=data) 
        if not id:
            raise forms.ValidationError("check the id")
            
        return cleaned_data