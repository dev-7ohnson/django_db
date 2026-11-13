from typing import Any

from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import Product
from myapp.my_forms import ProductForm

# Create your views here.
def home(request:Any):
    print("Home")
    products = Product.objects.all()
    for product in products:
        print(product.name, product.code, product.price, product.cost, product.category)
    return render(request, "home.html", {"products": products})


def add(request:Any):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()

    return render(request, "add.html", {"form": form})

    # Product.objects.create(name="Unga",
    #                        code="01004996",
    #                        price=2000,
    #                        cost=200,
    #                        category="Foods")

# create for a book with edit and delete buttons
def delete_product(request:Any, id):
    product = Product.objects.get(id=id) #select * from products where id = 86
    product.delete() #DELETE FROM PRODUCTS WHERE ID = 86
    return redirect('home')


def edit_product(request:Any, id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm(instance=product)

    return render(request, "edit.html", {"form": form})


def details_product(request:Any, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "details.html", {"product": product})