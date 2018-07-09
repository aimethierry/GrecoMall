from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(required=True ,label="", widget=forms.TextInput(
        attrs={'placeholder':"First name ", "class":"form-control"}
    ))

    last_name = forms.CharField(required=True ,label="", widget=forms.TextInput(
        attrs={'placeholder':"Last Name ", "class":"form-control"}
    ))



    email = forms.EmailField(required=True ,label="", widget=forms.TextInput(
        attrs={'placeholder':"Email", "class":"form-control"}
    ))


    address = forms.CharField(required=True ,label="", widget=forms.TextInput(
        attrs={'placeholder':"Address", "class":"form-control"}
    ))




    postal_code = forms.IntegerField(required=True ,label="", widget=forms.TextInput(
        attrs={'placeholder':"postal_code", "class":"form-control"}
    ))



    city = forms.CharField(required=True ,label="", widget=forms.TextInput(
        attrs={'placeholder':"city", "class":"form-control"}
    ))

    street = forms.CharField(required=True ,label="", widget=forms.TextInput(
        attrs={'placeholder':"street", "class":"form-control"}
    ))

    phone_number = forms.IntegerField()
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'street', 'phone_number']


        