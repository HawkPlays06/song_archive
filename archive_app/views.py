from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, "song_archive/home.html")

def log_in_view(request):
    return render(request, "song_archive/sign up.html")