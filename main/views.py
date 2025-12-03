from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from main.models import Product
from main.forms import ProductForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import datetime
import json
from django.urls import reverse

@login_required(login_url='/login/')
def show_main(request):
    filter_type = request.GET.get("filter", "all")

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

def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        form.save()
        return redirect("main:show_main")
    context = {"form": form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {"product": product}
    return render(request, "product_detail.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    filter_type = request.GET.get("filter", "all")
    
    if filter_type == "my" and request.user.is_authenticated:
        data = Product.objects.filter(user=request.user)
    else:
        data = Product.objects.all()
    
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    product = get_object_or_404(Product, pk=id)
    data = serializers.serialize("json", [product])
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
    context = {'form': form}
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

@login_required(login_url='/login/')
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

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

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_product = Product.objects.create(
            user=request.user,
            name=data["name"],
            price=int(data["price"]),
            description=data["description"],
            thumbnail=data["thumbnail"],
            category=data["category"],
            is_featured=bool(data["is_featured"]),
            stock=int(data["stock"]),
            brand=data.get("brand", ""),
            rating=float(data["rating"]),
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)