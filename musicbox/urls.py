from django.urls import path
import musicbox.views as views

urlpatterns = [
    path("", views.home, name='home'),
    path("playlist/new", views.create_playlist, name='create_playlist'),
    path("playlist/<int:playlist_id>", views.playlist_info, name='playlist_info'),
]