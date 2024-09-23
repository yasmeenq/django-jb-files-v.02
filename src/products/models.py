from django.db import models
from django.db.models import Model, CharField, DecimalField, IntegerField, ForeignKey, RESTRICT, DateField
from datetime import datetime

from django.forms import DateInput, ModelForm, NumberInput, Select, TextInput
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator

class CategoryModel(Model):
    # first column - id - will be created automatically 
    # second column 
    name = CharField(max_length=50)
    def __str__(self):
        return self.name
    #metadata
    class Meta: 
        db_table = "categories"



class ProductModel(Model):
    #first column id 
    #second column 
    name = CharField(max_length=50, validators=(MinLengthValidator(2), MaxLengthValidator(100)))
    #third column 
    price = DecimalField(max_digits=6, decimal_places=2, validators=(MinValueValidator(0, "I asked for the price to be more than 0"), MaxValueValidator(10000))) # 1023.34
    #fourth column 
    stock = IntegerField(validators=(MinValueValidator(2), MaxValueValidator(10000))) 
    #fifth column 
    category = ForeignKey(CategoryModel, on_delete=RESTRICT)
    #sixth column 
    release_date = DateField(default = datetime.now)
    class Meta: 
        db_table = "products"



class ProductForm(ModelForm):
    class Meta:
        model = ProductModel
        #fields = ["name", "price", "stock", "category", "release_date"]
        exclude = ["id"]
        widgets = {
            "name": TextInput(attrs = { "class": "form-control", "minlength": 2, "maxlength": 100 }), # attrs = HTML Attributes
            "price": NumberInput(attrs = { "class": "form-control", "min": 0, "max": 1000 }),
            "stock": NumberInput(attrs = { "class": "form-control", "min": 0, "max": 1000 }),
            "category": Select(attrs = { "class": "form-control" }),
            "release_date": DateInput(attrs = { "class": "form-control", "type": "date" }),
        }



class CategoryForm(ModelForm):
    class Meta:
        model = CategoryModel
        #fields = ["name"]
        exclude = ["id"]

        widgets = {
            "name": TextInput(attrs = { "class": "form-control", "minlength": 2, "maxlength": 100 }), # attrs = HTML Attributes
        }