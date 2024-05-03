from django import forms
from django.forms import fields
from .models import FoodItem


class Itemdetail(forms.ModelForm):
    class Meta:
        model=FoodItem
        fields="__all__"


    
    