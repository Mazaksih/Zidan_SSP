from django.shortcuts import render, redirect
from paket.forms import FormBarang
from paket.models import Barang
from django.contrib import messages

# Method untuk menambahkan data
def tambah_barang(request):
    form = FormBarang(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,"Data berhasil ditambahkan")
        form = FormBarang()
        konteks = {
            'form' : form,
        }
        return render(request,'tambah_barang.html',konteks)
    else:
        form=FormBarang()
        konteks = {
            'form' : form,
        }
    return render(request,'tambah_barang.html',konteks)

# Method untuk mengubah data
def ubah_brg(request,id_barang) :
    barangs=Barang.objects.get(id=id_barang)
    if request.POST:
        form=FormBarang(request.POST,instance=barangs)
        if form.is_valid():
            form.save()
            messages.success(request,"Data berhasil di ubah")
            return redirect('ubah_brg',id_barang=id_barang)
    else:
        form=FormBarang(instance=barangs)
        konteks = {
            'form':form,
            'barangs':barangs
        }
    return render(request,'ubah_brg.html',konteks)

# Method untuk menghapus data
def hapus_brg(request,id_barang):
    barangs=Barang.objects.filter(id=id_barang)
    barangs.delete()
    messages.success(request,"Data terhapus")
    return redirect('/Vbrg')

# Method untuk menampilkan data
def Barang_View(request):
    barangs=Barang.objects.all()

    konteks={
        'barangs':barangs,
    }
    return render(request, 'tampil_barang.html',konteks)