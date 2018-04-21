from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from .models import Album


# Create your views here.
def index(request):
    albums = Album.objects.all()
    return render(request , 'music/albumdetails.html' , {'albums': albums})



def albumdetails(request , id):
    try:
        album =  Album.objects.get(pk=id)
    except:
        raise Http404("No such Album exists.")

    return render(request , 'music/albumsongs.html' , {'album' : album} )