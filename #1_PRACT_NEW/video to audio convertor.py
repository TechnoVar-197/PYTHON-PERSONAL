from moviepy.editor import VideoFileClip

def convert_to_mp3(filename):
    clip = VideoFileClip(filename)
    clip.audio.write_audiofile(filename[:-4] + ".mp3")
    clip.close()
    print(done)
x = input("enter filename")
convert_to_mp3(x)
