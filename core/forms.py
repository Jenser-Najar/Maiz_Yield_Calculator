from django import forms
from .models import ProductionData

class ProductionDataForm(forms.ModelForm):
    class Meta:
        model = ProductionData
        fields = ['area_m2', 'seeds_per_m2', 'cobs_per_plant', 'price_per_cob']
