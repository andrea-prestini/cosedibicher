from pytube import YouTube
import os


yt = YouTube(
    str(input("Inserisci URL da scaricare: \n>> ")))

destination = str(input(">> ")) or "."
titolo = yt.title


video = yt.streams.get_highest_resolution()
video.download(destination)

# result of success
print(yt.title + "scaricato con successo!")
print(f'''
il file {yt.title}
occupa {os.system("du -h {}.mp4".format(titolo))/1000:,.2f} MB''')