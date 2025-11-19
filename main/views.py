from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from main.models import Product
from main.forms import ProductForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import datetime
import json


# Halaman utama menampilkan list produk
@login_required(login_url='/login/')
def show_main(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "my":
        products = Product.objects.filter(user=request.user)
    else:
        products = Product.objects.all()

    context = {
        "name": "Faishal Khoiriansyah Wicaksono",
        "class": "PBP D",
        "app_name": "Football Shop",
        "product_list": products,
        "last_login": request.COOKIES.get('last_login', 'Never'),
    }
    return render(request, "main.html", context)


# Form tambah produk
@login_required(login_url='/login/')
def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect("main:show_main")
    context = {"form": form}
    return render(request, "create_product.html", context)


# Detail produk
@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {"product": product}
    return render(request, "product_detail.html", context)


# Data Delivery - XML (All Products)
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


# Data Delivery - JSON
# PENTING: Endpoint ini untuk Flutter!
def show_json(request):
    """
    Return all products atau hanya milik user jika ada filter
    Untuk Flutter: tanpa login akan return semua produk
    """
    filter_type = request.GET.get("filter", "all")
    
    # Jika request dari authenticated user dan minta filter "my"
    if request.user.is_authenticated and filter_type == "my":
        data = Product.objects.filter(user=request.user)
    else:
        # Return all products untuk "All Products" page
        data = Product.objects.all()
    
    return HttpResponse(
        serializers.serialize("json", data), 
        content_type="application/json"
    )


def show_json_by_id(request, id):
    """
    Return single product by ID
    Digunakan untuk detail page di Flutter
    """
    product = get_object_or_404(Product, pk=id)
    data = serializers.serialize("json", [product])
    return HttpResponse(data, content_type="application/json")


def show_xml_by_id(request, id):
    product = get_object_or_404(Product, pk=id)
    data = serializers.serialize("xml", [product])
    return HttpResponse(data, content_type="application/xml")


# Register (Web)
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form': form}
    return render(request, 'register.html', context)


# Login (Web)
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)


# Logout (Web)
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response


# Edit Product
@login_required(login_url='/login/')
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("main:show_main")

    context = {
        "form": form,
        "product": product
    }
    return render(request, "edit_product.html", context)


# Delete Product
@login_required(login_url='/login/')
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))


# Add to Cart
@login_required(login_url='/login/')
def add_to_cart(request, id):
    product = get_object_or_404(Product, pk=id)

    if product.stock > 0:
        product.stock -= 1
        product.save()
        messages.success(request, f"{product.name} berhasil ditambahkan ke cart!")
    else:
        messages.error(request, f"{product.name} sudah habis stoknya!")

    return redirect("main:show_main")


# API untuk Flutter - Create Product
@csrf_exempt
@login_required(login_url='/login/')
def create_product_flutter(request):
    """
    Endpoint untuk create product dari Flutter
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            new_product = Product.objects.create(
                user=request.user,
                name=data["name"],
                price=int(data["price"]),
                description=data["description"],
                thumbnail=data["thumbnail"],
                category=data["category"],
                is_featured=data.get("is_featured", False),
                stock=int(data.get("stock", 0)),
                brand=data.get("brand", ""),
                rating=float(data.get("rating", 0.0))
            )

            new_product.save()

            return JsonResponse({
                "status": "success",
                "message": "Product created successfully!"
            }, status=200)

        except Exception as e:
            return JsonResponse({
                "status": "error",
                "message": str(e)
            }, status=500)
    
    return JsonResponse({
        "status": "error",
        "message": "Invalid request method"
    }, status=405)