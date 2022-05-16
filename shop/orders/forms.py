from django import forms

from .models import Order


class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["first_name", 'last_name', "email", "address", "city"]
        widgets ={
            "first_name": forms.TextInput(attrs={"class": "forms-control"}),
            "last_name": forms.TextInput(attrs={"class": "forms-control"}),
            "email": forms.EmailInput(attrs={"class": "forms-control"}),
            "address": forms.TextInput(attrs={"class": "forms-control"}),
            "city": forms.TextInput(attrs={"class": "forms-control"})
        }