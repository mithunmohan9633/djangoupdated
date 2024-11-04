from django import forms
from .models import CarForSale, CarForRent, OilType

class CarForSaleForm(forms.ModelForm):
    oil_type = forms.ChoiceField(choices=OilType.OIL_CHOICES, widget=forms.Select)
    brand = forms.CharField(max_length=100)

    class Meta:
        model = CarForSale
        exclude = ['user']  # Exclude the user field if not needed in form

class CarForRentForm(forms.ModelForm):
    class Meta:
        model = CarForRent
        fields = [
            'user', 
            'name', 
            'brand', 
            'oil_type', 
            'description', 
            'price_per_day', 
            'mileage', 
            'car_image', 
            'location', 
            'whatsapp_number', 
            'registration_number'
        ]

    oil_type = forms.ModelChoiceField(
        queryset=OilType.objects.all(),
        empty_label="Select Oil Type",
        to_field_name='name'  # Display the name of the oil type
    )
