from pytube import YouTube
import os

# url input from user
yt = YouTube(str(input("inserire URL da scaricare:\n")))

# video download
video = yt.streams.filter(only_audio=True).first()
titolo = yt.title

# check for destination to save file
destination = str(input(">> ")) or "."


# download the file
out_file = video.download(output_path=destination)

# save the file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)


# result of success
print(yt.title + " è stato scaricato con successo!")
print(f'''il file {yt.title}
occupa {os.system("du -h {}.mp4".format(titolo))/1000:,.2f} MB''')