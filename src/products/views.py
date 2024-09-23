from django.http import Http404
from django.shortcuts import render, redirect
from products.models import *

#we include facade here
 
# Create your views here.
def sales(request):
    context = {"active": "sales"}
    return render(request, "sales.html", context)


def list(request):
    products = ProductModel.objects.all()  #bring all products
    context = {"active": "products", "products": products}
    return render(request, "products.html", context)

def details(request, id):
    try:
        product = ProductModel.objects.get(pk=id)  #pk=primary key
        context = {"active": "details", "product": product}
        return render(request, "details.html", context)
    except ProductModel.DoesNotExist:
        raise Http404()

def categories(request):
    categories = CategoryModel.objects.all()
    context = {"active": "categories", "categories": categories}
    return render(request, "categories.html", context)


def insert(request):
    if request.method =="GET":
        context = {"active":"insert", "form":ProductForm()}
        return render(request, "insert.html", context)
    
    form = ProductForm(request.POST)
    if not form.is_valid():
        context = {"form": form}
        return render(request, "insert.html", context)
    form.save() 
    return redirect("products_route")


def insertCategory(request):
    if request.method =="GET":
        context = {"active":"insertCategory", "form":CategoryForm()}
        return render(request, "insertCategory.html", context)
    
    form = CategoryForm(request.POST)
    form.save() 
    return redirect("categories_route")

def edit(request, id):
    try:
        if request.method == "GET":
            product = ProductModel.objects.get(pk=id)
            context = {"form": ProductForm(instance=product)}
            return render(request, "edit.html", context)
        
        product = ProductModel.objects.get(pk=id)
        form = ProductForm(request.POST, instance=product)
        form.save()
        return redirect("products_route")
    except ProductModel.DoesNotExist:
        raise Http404()

def editCategory(request, id):
    try:
        if request.method == "GET":
            product = CategoryModel.objects.get(pk=id)
            context = {"form": CategoryForm(instance=product)}
            return render(request, "editCategory.html", context)
        
        product = CategoryModel.objects.get(pk=id)
        form = CategoryForm(request.POST, instance=product)
        form.save()
        return redirect("categories_route")
    except ProductModel.DoesNotExist:
        raise Http404()

def delete(request, id):
    try:
        if request.method == "GET":
            product = ProductModel.objects.get(pk=id)
            product.delete()
            return redirect("products_route")
    except ProductModel.DoesNotExist:
        raise Http404()
    
def deleteCategory(request, id):
    try:
        if request.method == "GET":
            product = CategoryModel.objects.get(pk=id)
            product.delete()
            return redirect("categories_route")
    except ProductModel.DoesNotExist:
        raise Http404()        