from pathlib import Path
from pytube import YouTube

list = []
print("Enter URLs (terminate = 'STOP')")
while True:
    url = input("")
    if url == "STOP":
        break
    list.append(url)

for link in list:
    video = YouTube(link)
    for stream in video.streams:  # the video can be many different types of things that have even more things in it. Ex: It can be an mp4 with a resolution of 1080p with 30 fps
        print(stream)
    num = input("\nplease pick an itag # for " + video.title + ": ")
    stream = video.streams.get_by_itag(num)  # 18 is 360p with 30 fps
    name = input("Would you like to name this song? (you should change the name just in case of an error): ")
    print("Downloading...")
    stream.download(filename=name)  # in the parameters - filename="download_name"
    print("Done")
    p = Path(name + ".mp4")  # you can get rid of line 19 and 20 if you don't want to download it to an mp3
    p.rename(p.with_suffix(".mp3"))

'''
for stream in video.streams: # the video can be many different types of things that have even more things in it. Ex: It can be an mp4 with a resolution of 1080p with 30 fps
    print(stream)
'''
