from pytube import YouTube
from pytube import Playlist

def downvideo(url):
    yt = YouTube(url)
    print('Descargando: ', yt.title)
    stream = yt.streams.get_highest_resolution()
    stream.download('Descargas')


tipo = input('1. Video or 2. Playlist: ')

if (tipo == '1'):
    url = input('URL video: ')
    downvideo(url) 
    
elif(tipo == '2'):
    url = input('URL playlist: ')
    p = Playlist(url)
    print('Lista: ', p.title)
    todos = input ('Descargar todos los videos(s/n)? ')
    print('')
    
    if (todos == 's'):
        for video in p.videos:
            print('Descargando: ', video.title)
            video.streams.get_highest_resolution().download(p.title)
            
    elif (todos == 'n'):
        option = input('1. Obtener URLs videos or 2. Descargar intervalo de videos: ')
        print('')
        if (option == '1'):
            lista = []
            for url in p.video_urls:
                lista.append(url)

            print(lista)
            
        if (option == '2'):
            intervalo = input('Indica intervalo (numero video inicial y numero video final, separdos por espacio): ').split()
            print('')
        
            for i in range(int(intervalo[0]) - 1, int(intervalo[1])):
                print('Descargando: ', p.videos[i].title)
                p.videos[i].streams.get_highest_resolution().download(p.title)

    else:
        print('Selección erronea')

else:
     print('Selección erronea')
