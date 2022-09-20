"""mis_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from  akademik import views as akademikViews
from  mahasiswa import views as mahasiswaViews
from  instruktur import views as dosenViews
from  accounting import views as accViews

urlpatterns = [
    # modul dashboard
    path('', views.index),
    
    path('admin/', admin.site.urls),
    
    path('login/', views.login),

    path('presensi/', views.presensi),
    path('registrasi/', views.registrasi),
    path('forgot/', views.forgot),
    
   
    
    # modul akademik
    path('kalender_akademik/', akademikViews.kalender_list),
    path('kalender_akademik/unggah', akademikViews.kalender_upload),

    # modul jadwal pelajaran
    path('jadwal_pelajaran/', akademikViews.jadwal_pelajaran_list),
    path('jadwal_pelajaran/add', akademikViews.jadwal_pelajaran_add),

    # modul biodata_sistem
    path('biodata_siswa/', akademikViews.biodata_list),
    path('biodata_siswa/view', akademikViews.biodata_view),

    # modul profil kompetensi
    path('kompetensi/', akademikViews.kompetensi_list),
    path('kompetensi/add', akademikViews.kompetensi_add),
    path('kompetensi/view', akademikViews.kompetensi_view),

 # modul dosen
    path('dosen/', akademikViews.dosen_list),
    path('dosen/add', akademikViews.dosen_add),
    
 # modul berkas dosen
    path('berkas_dosen/', akademikViews.berkas_dosen_list),
    path('berkas_dosen/add', akademikViews.berkas_dosen_add),
    
 # modul surat
    path('surat/', akademikViews.surat_list),
    path('surat/add', akademikViews.surat_add),

# modul bst_passport
    path('bst_passport/', akademikViews.bst_passport_list),
    path('bst_passport/add', akademikViews.bst_passport_add), 
    
# modul perubahan password
    path('password/', mahasiswaViews.password),
    
# modul tracking
    path('tracking/', mahasiswaViews.tracking),

# modul nilai dan Sertifikat
    path('nilai_sertifikat/', mahasiswaViews.nilai_sertifikat),
    
# modul materi kuliah
    path('materi_kuliah/', dosenViews.materi_kuliah_list),
    path('materi_kuliah/add', dosenViews.materi_kuliah_add),

# modul input nilai ujian
    path('nilai_ujian/', dosenViews.nilai_ujian),

# modul pembayaran mahasiswa
    path('pembayaran/', accViews.pembayaran),
    
# modul laporan keuangan
    path('laporan_keuangan/', accViews.laporan_keuangan),
# modul tampil biodata siswa
    path('biodata_siswa/view', mahasiswaViews.biodata_view),
# modul tampil biodata dosen
    path('biodata_dosen/view', dosenViews.biodata_view)
]
