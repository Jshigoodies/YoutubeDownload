import pytube
from pathlib import Path

list = []
print("Enter URLs (terminate = 'STOP')")
while True:
    url = input("")
    if url == "STOP":
        break
    list.append(url)

for link in list:
    video = pytube.YouTube(link)
    print(video.title)
    stream = video.streams.get_by_itag(140) # 18 is 360p with 30 fps
    print("Downloading...")
    stream.download() # in the parameters - filename="download_name"
    print("Done")
    p = Path(video.title + ".mp4")  # you can get rid of line 19 and 20 if you don't want to download it to an mp3
    p.rename(p.with_suffix(".mp3"))

'''
for stream in video.streams: # the video can be many different types of things that have even more things in it. Ex: It can be an mp4 with a resolution of 1080p with 30 fps
    print(stream)
'''