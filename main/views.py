from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from main.models import Product
from main.forms import ProductForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse
import json

# Halaman utama menampilkan list produk
@login_required(login_url='/login/')
def show_main(request):
    context = {
        "name": "Faishal Khoiriansyah Wicaksono",
        "class": "PBP D",
        "app_name": "Football Shop",
        "last_login": request.COOKIES.get('last_login', 'Never'),
    }
    return render(request, "main.html", context)

# API: Get products (AJAX)
@login_required(login_url='/login/')
def get_products_json(request):
    filter_type = request.GET.get("filter", "all")
    
    if filter_type == "my":
        products = Product.objects.filter(user=request.user)
    else:
        products = Product.objects.all()
    
    data = []
    for product in products:
        data.append({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'stock': product.stock,
            'brand': product.brand,
            'rating': product.rating,
            'user': product.user.username if product.user else 'Anonymous',
            'is_owner': product.user == request.user if product.user else False,
        })
    
    return JsonResponse({'products': data}, safe=False)

# API: Create product (AJAX)
@csrf_exempt
@require_POST
@login_required(login_url='/login/')
def create_product_ajax(request):
    try:
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        thumbnail = request.POST.get("thumbnail")
        category = request.POST.get("category")
        is_featured = request.POST.get("is_featured") == "on"
        stock = request.POST.get("stock")
        brand = request.POST.get("brand")
        rating = request.POST.get("rating")
        
        product = Product.objects.create(
            user=request.user,
            name=name,
            price=price,
            description=description,
            thumbnail=thumbnail,
            category=category,
            is_featured=is_featured,
            stock=stock,
            brand=brand,
            rating=rating
        )
        
        return JsonResponse({
            "status": "success",
            "message": "Product created successfully!",
            "product": {
                'id': product.id,
                'name': product.name,
                'price': product.price,
            }
        }, status=201)
    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": str(e)
        }, status=400)

# API: Update product (AJAX)
@csrf_exempt
@require_POST
@login_required(login_url='/login/')
def update_product_ajax(request, id):
    try:
        product = get_object_or_404(Product, pk=id, user=request.user)
        
        product.name = request.POST.get("name")
        product.price = request.POST.get("price")
        product.description = request.POST.get("description")
        product.thumbnail = request.POST.get("thumbnail")
        product.category = request.POST.get("category")
        product.is_featured = request.POST.get("is_featured") == "on"
        product.stock = request.POST.get("stock")
        product.brand = request.POST.get("brand")
        product.rating = request.POST.get("rating")
        product.save()
        
        return JsonResponse({
            "status": "success",
            "message": "Product updated successfully!"
        })
    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": str(e)
        }, status=400)

# API: Delete product (AJAX)
@csrf_exempt
@require_POST
@login_required(login_url='/login/')
def delete_product_ajax(request, id):
    try:
        product = get_object_or_404(Product, pk=id, user=request.user)
        product_name = product.name
        product.delete()
        
        return JsonResponse({
            "status": "success",
            "message": f"{product_name} deleted successfully!"
        })
    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": str(e)
        }, status=400)

# API: Login (AJAX)
@csrf_exempt
def login_ajax(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return JsonResponse({
                "status": "success",
                "message": "Login successful!",
                "username": user.username
            })
        else:
            return JsonResponse({
                "status": "error",
                "message": "Invalid username or password"
            }, status=401)
    
    return JsonResponse({
        "status": "error",
        "message": "Invalid request method"
    }, status=400)

# API: Register (AJAX)
@csrf_exempt
def register_ajax(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            return JsonResponse({
                "status": "error",
                "message": "Passwords do not match"
            }, status=400)
        
        if len(password1) < 8:
            return JsonResponse({
                "status": "error",
                "message": "Password must be at least 8 characters"
            }, status=400)
        
        from django.contrib.auth.models import User
        if User.objects.filter(username=username).exists():
            return JsonResponse({
                "status": "error",
                "message": "Username already exists"
            }, status=400)
        
        try:
            user = User.objects.create_user(username=username, password=password1)
            user.save()
            return JsonResponse({
                "status": "success",
                "message": "Registration successful!"
            })
        except Exception as e:
            return JsonResponse({
                "status": "error",
                "message": str(e)
            }, status=400)
    
    return JsonResponse({
        "status": "error",
        "message": "Invalid request method"
    }, status=400)

# Keep old views for fallback
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
    context = {
        "product": product,
        "is_owner": product.user == request.user if product.user else False,
    }
    return render(request, "product_detail.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
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
    context = {"form": form, "product": product}
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


# API: Get single product detail (AJAX)
@login_required(login_url='/login/')
def get_product_detail_json(request, id):
    try:
        product = get_object_or_404(Product, pk=id)
        data = {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'stock': product.stock,
            'brand': product.brand,
            'rating': product.rating,
            'user': product.user.username if product.user else 'Anonymous',
            'is_owner': product.user == request.user if product.user else False,
        }
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": str(e)
        }, status=400)