from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import ProductReview, Product


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')



class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ('review',)


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'product_image', 'category')

