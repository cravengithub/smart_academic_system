from django.shortcuts import render

# Create your views here.
def kalender_list(request):
    return render(request, 'kalender_akademik/list.html')
def kalender_upload(request):
    return render(request, 'kalender_akademik/upload.html')

def jadwal_pelajaran_list(request):
    return render(request, 'jadwal_pelajaran/list.html')
def jadwal_pelajaran_add(request):
    return render(request, 'jadwal_pelajaran/form.html')

def biodata_list(request):
    return render(request, 'biodata_siswa/list.html')
def biodata_view(request):
    return render(request, 'biodata_siswa/view.html')

def kompetensi_list(request):
    return render(request, 'profil_kompetensi/list.html')
def kompetensi_view(request):
    return render(request, 'profil_kompetensi/view.html')
def kompetensi_add(request):
    return render(request, 'profil_kompetensi/form.html')

def dosen_list(request):
    return render(request, 'dosen/list.html')
def dosen_add(request):
    return render(request, 'dosen/form.html')   
    
def berkas_dosen_list(request):
    return render(request, 'berkas_dosen/list.html')
def berkas_dosen_add(request):
    return render(request, 'berkas_dosen/form.html')    
    
def surat_list(request):
    return render(request, 'surat/list.html')
def surat_add(request):
    return render(request, 'surat/form.html') 
    
def bst_passport_list(request):
    return render(request, 'bst_passport/list.html')
def bst_passport_add(request):
    return render(request, 'bst_passport/form.html') 
    