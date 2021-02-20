from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'covidback/index.html')

def video1(request):
    return render(request, 'covidback/videos.html')

def video2(request):
    return render(request, 'covidback/video2.html')

def videoindex(request):
    return render(request, 'covidback/videoindex.html')

def overview(request):
    return render(request, 'covidback/overview.html')


