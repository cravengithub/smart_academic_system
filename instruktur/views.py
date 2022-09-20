from django.shortcuts import render

# Create your views here.
# Create your views here.
def materi_kuliah_list(request):
    return render(request, 'materi_kuliah/list.html')
def materi_kuliah_add(request):
    return render(request, 'materi_kuliah/form.html')
def nilai_ujian(request):
    return render(request, 'nilai_ujian/list.html')
def biodata_view(request):
    return render(request, 'biodata_dosen/view.html')