
from django import forms
from .models import User
class ProductDetails(forms.ModelForm):
    class Meta:
        model = User
        fields = ['Product_Name','Price','Quantity']
        widgets = {
            'Product_Name' :forms.TextInput(attrs={'class':'form-control'}),
            'Price' :forms.NumberInput(attrs={'class':'form-control'}),
            'Quantity' :forms.NumberInput(attrs={'class':'form-control'}) 
        }
