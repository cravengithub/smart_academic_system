from django.shortcuts import render

# Create your views here.
def pembayaran(request):
    return render(request, 'pembayaran/list.html')
    
def laporan_keuangan(request):
    return render(request, 'laporan_keuangan/list.html')