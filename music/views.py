from django.shortcuts import render, get_object_or_404, redirect
from .models import Album
from .forms import AlbumForm


def album_list(request):
    albums = Album.objects.all()
    return render(request, 'music/album_list.html', {'albums': albums})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'music/album_detail.html', {'album': album})


def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    album.delete()
    return redirect('album_list')


def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "GET":
        context = {'form': AlbumForm(instance=album), 'pk': pk}
    else:
        form = AlbumForm(request.POST)
        form.save()
        return redirect('album-list')
    return render(request, 'music/edit_album.html', context)


def create_album(request):
    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(request.POST)
        form.save()
        return redirect('album_list')
    return render(request, 'music/new_album.html', {'form': form})
