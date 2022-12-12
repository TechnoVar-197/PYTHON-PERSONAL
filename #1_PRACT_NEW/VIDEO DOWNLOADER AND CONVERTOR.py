import pytube
from moviepy.editor import VideoFileClip

def convert_to_mp3():
    video_list = []
    name_list = []
    res_list = []
    ita = 0
    while True:
        url = input("enter URL'S (TERMINATE BY STOP):--")
        if url == "STOP" or url == "stop" or url == "Stop":
            break
        nam = input("enter name of above url:--")
        print("PLEASE CHECK THAT VIDEO HAS SAME RESOLUTION AVAILABLE AS YOU ARE GOING SELECT")
        res = input("Enter resolution for video(4k/1080p/720p/480p/360p/240p/144p)")
        video_list.append(url)
        name_list.append(nam)
        res_list.append(res)
    for x, video in enumerate(video_list):
        vid = pytube.YouTube(video)
        name = name_list[x]
        res = res_list[x]
        if res == "4k" or res == "4K":
            ita = 313
        if res == "1080p" or res == "1080P":
            ita = 137
        if res == "720p" or res == "720P":
            ita = 22
        if res == "480p" or res == "480P":
            ita = 135
        if res == "360p" or res == "360P":
            ita = 18
        if res == "240p" or res == "240P":
            ita = 133
        if res == "144p" or res == "144P":
            ita = 160
        stream = vid.streams.get_by_itag(ita)
        print(f"Downloading video {x + 1} {name} ....")
        stream.download(filename=name)
        print("Video downloaded")
        print("converting......")
        fna = name + ".mp4"
        clip = VideoFileClip(fna)
        clip.audio.write_audiofile(name[:-4] + ".mp3")
        clip.close()
        print("Done")
def sig_vid():
    video_list = []
    name_list = []
    res_list = []
    it = 0
    while True:
        url = input("enter URL'S (TERMINATE BY STOP):--")
        if url == "STOP" or url == "stop" or url == "Stop":
            break
        nam = input("enter name of above url:--")
        print("PLEASE CHECK THAT VIDEO HAS SAME RESOLUTION AVAILABLE AS YOU ARE GOING SELECT")
        res = input("Enter resolution for video(4k/1080p/720p/480p/360p/240p/144p)")
        video_list.append(url)
        name_list.append(nam)
        res_list.append(res)
    for x , video in enumerate(video_list):
        vid = pytube.YouTube(video)
        name = name_list[x]
        res = res_list[x]
        if res == "4k" or res == "4K":
            it = 313
        if res == "1080p" or res == "1080P":
            it = 137
        if res == "720p" or res == "720P":
            it = 2
        if res == "480p" or res == "480P":
            it = 135
        if res == "360p" or res == "360P":
            it = 18
        if res == "240p" or res == "240P":
            it = 133
        if res == "144p" or res == "144P":
            it = 160
        stream = vid.streams.get_by_itag(it)
        print(f"Downloading video {x+1} {name} ....")
        stream.download(filename=name)
        print("Done")
def vid_playlist():
    it = 0
    url = input("enter playlist url:--")
    play = pytube.Playlist(url)
    print("PLEASE CHECK THAT EACH VIDEO HAS SAME RESOLUTION AVAILABLE AS YOU ARE GOING SELECT")
    res = input("Enter resolution for video(4k/1080p/720p/480p/360p/240/144p)")
    if res == "4k" or res == "4K":
        it = 313
    if res == "1080p" or res == "1080P":
        it = 137
    if res == "720p" or res == "720P":
        it = 2
    if res == "480p" or res == "480P":
        it = 135
    if res == "360p" or res == "360P":
        it = 18
    if res == "240p" or res == "240P":
        it = 133
    if res == "144p" or res == "144P":
        it = 160
    for url in play:
        vid = pytube.YouTube(url)
        stream = vid.streams.get_by_itag(it)
        stream.download()
        print("playlist downloaded")

print('What do you want?')
print("(1) Download YouTube Videos Manually")
print("(2) Download a YouTube Playlist")
print("(3) Download YouTube Videos and Convert Into MP3 ")
ch = int(input("enter choice:-"))
if ch == 1:
    sig_vid()
elif ch == 2:
    vid_playlist()
elif ch == 3:
    convert_to_mp3()
else:
    print("please choose from given options")
