from pytube import YouTube
import ffmpeg
import os

raw = 'C:\ProgramData\ytChache'

path1 = 'C:\ProgramData\ytChache\Video\\'
path2 = 'C:\ProgramData\ytChache\Audio\\'

file_type = "mp4"

if os.path.exists(path1 and path2):
    boo = True
else:
    boo = False

while boo:

    url = str(input("Link : "))
    choice = int(input('Enter 1 for Only Audio and Enter 2 For Both Audio and Video \n: '))

    video = YouTube(url)
    Streams = video.streams

    if choice == 1:
        aud = Streams.filter(only_audio=True).first().download(path2)

    elif choice == 2:
        resol = str(input("Resolution : "))
        vid = Streams.filter(res=resol, file_extension=file_type).first().download(path1)
        aud = Streams.filter(only_audio=True).first().download(path2)

        file = video.title + '.mp4'
        # location = path1
        # location2 = path2
        rem = os.path.join(path1, file)
        rm = os.path.join(path2, file)

        video_stream = ffmpeg.input(path1, video.title + '.mp4')
        audio_stream = ffmpeg.input(path2, video.title + '.mp4')
        ffmpeg.output(audio_stream, video_stream, video.title + '.mp4').run()
        os.remove(rem)
        os.remove(rm)

    else:
        print('Invalid Selection')

if not boo:
    os.mkdir(raw)
    os.mkdir(path1)
    os.mkdir(path2)