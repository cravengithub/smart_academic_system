from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'base.html')
def login(request):
    return render(request, 'login.html')
def presensi(request):
    return render(request, 'presensi.html')
def registrasi(request):
    return render(request, 'register.html')
def forgot(request):
    return render(request, 'forgot-password.html')