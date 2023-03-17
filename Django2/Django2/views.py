from django.http import HttpResponse
from django.shortcuts import render

def main(request):
    return render(request, 'main.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def ourworks(request):
    return render(request, 'ourworks.html')

def contacts(request):
    return render(request, 'contacts.html')

