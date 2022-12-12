import pytube

video_list = []
while True:
    url = input("enter URL'S (TERMINATE BY STOP)")
    if url == "STOP" or url == "stop" or url == "Stop":
        break
    video_list.append(url)
for x , video in enumerate(video_list):
    vid = pytube.YouTube(video)
    nam = input(f"enter file name for above url: {video}")
    res = input(f"Enter resolution for video {x+1}(1080p/720p/480p/360p/240p/144p")
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
        ita == 160
    stream = vid.streams.get_by_itag(ita)
    print(f"Downloading video {x+1} {nam} ....")
    stream.download(filename=nam)
    print("Done")
