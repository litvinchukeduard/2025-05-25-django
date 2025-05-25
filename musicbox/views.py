from django.shortcuts import render, redirect
from musicbox.models import Playlist

# Create your views here.
def home(request):
    playlists_list = Playlist.objects.all()
    return render(request, 'index.html', {'playlists': playlists_list})

def create_playlist(request):
    if request.method == 'POST':
        name = request.POST.get('playlist_name')
        if name:
            Playlist.objects.create(name=name)
        return redirect('home')
    elif request.method == 'GET':
        return render(request, 'create_playlist.html')
    
def playlist_info(request, playlist_id: int):
    if request.method == 'POST':
        ...
    playlist = Playlist.objects.get(id=playlist_id)
    return render(request, 'playlist_info.html', {'playlist': playlist})
