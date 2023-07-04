from django.contrib import admin
from django.urls import path
from paket.views import *

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('paket/',views.paket),
    path('addbrg/',tambah_barang),
    path('Vbrg/',Barang_View),
    path('ubah/<int:id_barang>',ubah_brg,name='ubah_brg'),
    path('hapus/<int:id_barang>',hapus_brg,name='hapus_brg'),
]
