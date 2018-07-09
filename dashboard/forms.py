from django import forms 
from product.models import Category, Product

class CategoryForm(forms.ModelForm):
    name = forms.CharField(label='', 
                widget=forms.TextInput(
                        attrs={'placeholder': "Enter a category", 
                            "class": "form-control"}
                    ))


    slug = forms.CharField(label='', 
                widget=forms.TextInput(
                        attrs={'placeholder': "Enter a slug", 
                            "class": "form-control"}
                    ))
    class Meta:
        model = Category
        fields = [
            'name',
            'slug',
            "image",   
        ]



class ProductForm(forms.ModelForm):
    name = forms.CharField(label='', 
                widget=forms.TextInput(
                        attrs={'placeholder': "Enter a category", 
                            "class": "form-control"}
                    ))


    slug = forms.CharField(label='', 
                widget=forms.TextInput(
                        attrs={'placeholder': "Enter a slug", 
                            "class": "form-control"}
                    ))




    description = forms.CharField(label='', 
                widget=forms.Textarea(
                        attrs={'placeholder': "Describe the Product", 
                            "class": "form-control"}
                    ))


    addition = forms.CharField(label='', 
                widget=forms.Textarea(
                        attrs={'placeholder': "Add addtional description of the product", 
                            "class": "form-control"}
                    ))


    price = forms.IntegerField()

    stock = forms.IntegerField()


    class Meta:
        model = Product
        fields = [
            'category',
            'name',
            'slug',
            'description',
            'addition',
            'price',
            'stock',
            "image", 

        ]