from django.shortcuts import render

# Create your views here.
def password(request):
    return render(request, 'password/form.html')
    
def tracking(request):
    return render(request, 'tracking/list.html')
    
def nilai_sertifikat(request):
    return render(request, 'nilai_sertifikat/list.html')

def biodata_view(request):
    return render(request, 'biodata_siswa/view.html')