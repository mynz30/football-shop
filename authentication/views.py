from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json


@csrf_exempt
def login(request):
    """
    Handle login dari Flutter
    """
    if request.method != 'POST':
        return JsonResponse({
            "status": False,
            "message": "Invalid request method."
        }, status=405)
    
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    if not username or not password:
        return JsonResponse({
            "status": False,
            "message": "Username and password are required."
        }, status=400)
    
    user = authenticate(username=username, password=password)
    
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Login sukses!"
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)
    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali username atau password."
        }, status=401)


@csrf_exempt
def register(request):
    """
    Handle register dari Flutter
    """
    if request.method != 'POST':
        return JsonResponse({
            "status": False,
            "message": "Invalid request method."
        }, status=405)
    
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({
            "status": False,
            "message": "Invalid JSON format."
        }, status=400)
    
    username = data.get('username')
    password1 = data.get('password1')
    password2 = data.get('password2')
    
    # Validasi input
    if not username or not password1 or not password2:
        return JsonResponse({
            "status": False,
            "message": "All fields are required."
        }, status=400)
    
    if password1 != password2:
        return JsonResponse({
            "status": False,
            "message": "Passwords do not match."
        }, status=400)
    
    if len(password1) < 8:
        return JsonResponse({
            "status": False,
            "message": "Password must be at least 8 characters long."
        }, status=400)
    
    if User.objects.filter(username=username).exists():
        return JsonResponse({
            "status": False,
            "message": "Username already exists."
        }, status=400)
    
    # Buat user baru
    try:
        user = User.objects.create_user(username=username, password=password1)
        user.save()
        
        return JsonResponse({
            "username": user.username,
            "status": 'success',
            "message": "User created successfully!"
        }, status=200)
    except Exception as e:
        return JsonResponse({
            "status": False,
            "message": f"Error creating user: {str(e)}"
        }, status=500)


@csrf_exempt
def logout(request):
    """
    Handle logout dari Flutter
    """
    username = request.user.username if request.user.is_authenticated else "Guest"
    
    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except Exception as e:
        return JsonResponse({
            "status": False,
            "message": f"Logout gagal: {str(e)}"
        }, status=500)