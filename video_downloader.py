from pytube import YouTube
import os
cwd = os.getcwd()
url = "https://youtu.be/Cvdhwx-OBBo"
yt = YouTube(url)

audio = yt.streams.filter(only_audio = True).first()
downloaded_file = audio.download(output_path = f"./audio/")
base, ext = os.path.splitext(downloaded_file)
new_file = os.path.join("audio", base + '.mp3')
os.rename(downloaded_file, new_file)
print("title:", yt.title)
print("Done")