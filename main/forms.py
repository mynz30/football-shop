from django.forms import ModelForm
from main.models import Product, Car

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "thumbnail", "category", "is_featured", "stock", "brand", "rating"]

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ["name", "brand", "stock"]
        #eee