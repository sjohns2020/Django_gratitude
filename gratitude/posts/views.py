from django.shortcuts import render

# Create your views here.

def list(request):
    return render(request, 'posts/list.html')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')