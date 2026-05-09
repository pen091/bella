from django.shortcuts import render, redirect
from .forms import PhotoForm
from .models import Photo

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = PhotoForm()

    photos = Photo.objects.all().order_by('-upload_at')
    return render(request, 'index.html', {'form': form, 'photos': photos})


