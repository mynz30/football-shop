from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Faishal Khoiriansyah Wicaksono',
        'class': 'PBP D',
        'app_name': 'Football Shop'
    }
    return render(request, "main.html", context)
