from django.shortcuts import render
from django.conf.urls.static import static


# Ini adalah method yang digunakan untuk memanggil data dari file index.html
def index(request):
    return render(request,'index.html')

def paket(request):
    return render(request,'paket.html')


