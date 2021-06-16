from pytube import YouTube
from pytube import Playlist

tipo = input('1. Video or 2. Playlist: ')
url = input('URL: ')
print('')

if (tipo == '1'):
    yt = YouTube(url)
    print('Descargando: ', yt.title)
    stream = yt.streams.get_highest_resolution()
    stream.download('Descargas')
    
else:
    p = Playlist(url)
    print('Descargando lista: ', p.title)
    todos = input ('Todos (s/n)? ')
    print('')
    
    if (todos == 's'):
        for video in p.videos:
            print('Descargando: ', video.title)
            video.streams.get_highest_resolution().download(p.title)
            
    else:
        intervalo = input('Indica intervalo (numero video inicial y numero video final, separdos por espacio): ').split()
        print('')
        
        for i in range(int(intervalo[0]) - 1, int(intervalo[1])):
            print('Descargando: ', p.videos[i].title)
            p.videos[i].streams.get_highest_resolution().download(p.title)
            