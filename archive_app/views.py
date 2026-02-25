from django.shortcuts import render

# Create your views here.
def testing_view(request):
    return render(request, "song_archive/base.html")