from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from main.models import Product
from main.forms import ProductForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse

# Halaman utama menampilkan list produk
@login_required(login_url='/login/')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # ✅ diperbaiki

    if filter_type == "all":
        products = Product.objects.all()
    else:
        products = Product.objects.filter(user=request.user)

    context = {
        "name": "Faishal Khoiriansyah Wicaksono",
        "class": "PBP D",
        "app_name": "Football Shop",
        "product_list": products,
        "last_login": request.COOKIES.get('last_login', 'Never'),
    }
    return render(request, "main.html", context)

# Form tambah produk
def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        form.save()
        return redirect("main:show_main")
    context = {"form": form}
    return render(request, "create_product.html", context)

# Detail produk
@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {"product": product}
    return render(request, "product_detail.html", context)

# Data Delivery - XML
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# Data Delivery - JSON
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    # Cari product berdasarkan ID, kalau tidak ada -> return 404
    product = get_object_or_404(Product, pk=id)
    data = serializers.serialize("json", [product])  # bungkus dalam list
    return HttpResponse(data, content_type="application/json")

def show_xml_by_id(request, id):
    product = get_object_or_404(Product, pk=id)
    data = serializers.serialize("xml", [product])
    return HttpResponse(data, content_type="application/xml")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

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

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login/')
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)  # hanya bisa edit produk milik user
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("main:show_main")

    context = {
        "form": form,
        "product": product
    }
    return render(request, "edit_product.html", context)

@login_required(login_url='/login/')
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)  # hanya pemilik produk yg bisa hapus
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@login_required(login_url='/login/')
def add_to_cart(request, id):
    product = get_object_or_404(Product, pk=id)

    # contoh logika dasar
    if product.stock > 0:
        product.stock -= 1
        product.save()
        messages.success(request, f"{product.name} berhasil ditambahkan ke cart!")
    else:
        messages.error(request, f"{product.name} sudah habis stoknya!")

    return redirect("main:show_main")
