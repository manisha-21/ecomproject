from django import forms
from .models import Order, Customer, Product
from django.contrib.auth.models import  User 


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["ordered_by", "shipping_address", "mobile", "email", "payment_method"]


class CustomerRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(widget=forms.EmailInput())

    class Meta:
        model = Customer
        fields =["username", "password", "email", "full_name", "address"]     

    def clean_username(self):
        uname = self.cleaned_data.get("username")
        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError("customer with this username already exists")

        return uname


class CustomerLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class ProductForm(forms.ModelForm):
    more_images = forms.FileField(required=False, widget=forms.FileInput(attrs={
        "class": "forms-control",
        "multiple": True
    }))
    class Meta:
        model = Product
        fields = ["title", "slug", "category", "image", "marked_price", "selling_price", "description", "warrantly", "return_policy"]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "forms-control",
                "placeholder": "Enter the product title here.."
            }),
            "slug": forms.TextInput(attrs={
                "class": "forms-control",
                "placeholder": "Enter the unique slug here.."
            }),
            "category": forms.Select(attrs={
                "class": "forms-control"
            }),
            "image": forms.ClearableFileInput(attrs={
                "class": "forms-control"
            }),
            "marked_price": forms.NumberInput(attrs={
                "class": "forms-control",
                "placeholder": "Marked price of the product.."
            }),
            "selling_price": forms.NumberInput(attrs={
                "class": "forms-control",
                "placeholder": "Selling price of the product.."
            }),
            "description": forms.Textarea(attrs={
                "class": "forms-control",
                "placeholder": "description of the product..",
                "row": 5
            }),
            "warrantly": forms.TextInput(attrs={
                "class": "forms-control",
                "placeholder": "Enter the product warrantly here.."
            }),
            "return_policy": forms.TextInput(attrs={
                "class": "forms-control",
                "placeholder": "Enter the product return policy here.."
            })   
        }