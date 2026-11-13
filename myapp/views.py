from typing import Any
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import Product
from myapp.my_forms import ProductForm

@login_required
def home(request: Any):
    print("Home")
    products = Product.objects.all()
    for product in products:
        print(product.name, product.code, product.price, product.cost, product.category)
    return render(request, "home.html", {"products": products})

@login_required
def add(request: Any):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Product successfully added")
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, "add.html", {"form": form})

@login_required
def delete_product(request: Any, id: int):
    product = get_object_or_404(Product, id=id)
    product.delete()
    messages.success(request, "Product deleted")
    return redirect('home')

@login_required
def edit_product(request: Any, id: int):
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully")
            return redirect('home')
    else:
        form = ProductForm(instance=product)
    return render(request, "edit.html", {"form": form})

@login_required
def details_product(request: Any, id: int):
    product = get_object_or_404(Product, id=id)
    return render(request, "details.html", {"product": product})


#groups created and assign permission in admin
def signin(request    ):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful")
            return redirect('home')
        else:
            form = AuthenticationForm()
        return render(request, "registration/login.html", {"form": form})
    return None

@login_required
def signout(request):
     if request.method == "POST":
         signout(request)
     return redirect('login')


def signup():
    return None