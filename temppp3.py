import tkinter
import customtkinter as ctk
from pytube import YouTube
import os
import emoji
import webbrowser
import ffmpeg


# location for downloading
DOWNLOAD_FOLDER = f"{os.getenv('USERPROFILE')}\\Downloads"
# CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
## DOWNLOADS_DIRECTORY = os.path.join(CURRENT_DIRECTORY, "Downloads")


def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

def startdownload():
    try:
        # ytLink = link.get()
        # ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        # title.configure(text=ytObject.title, text_color="white")
        # audio = ytObject.streams.filter(abr="160kbps", progressive=False).first().download(filename="audio.mp3")
        # video = ytObject.streams.filter(res="1080p", progressive=False).first().download(filename="video.mp4")
        # video.download(DOWNLOAD_FOLDER)
        # audio.download(DOWNLOAD_FOLDER)
        # finishLabel.configure(text="")
        ffmpeg_audio = ffmpeg.input('audio.mp3')
        ffmpeg_video = ffmpeg.input('video.mp4')
        # ffmpeg.output(ffmpeg_audio, ffmpeg_video, "finished_video.mp4").run(overwrite_output=True)
        ffmpeg.concat(ffmpeg_audio, ffmpeg_video, v=1, a=1).output('finished_video.mp4').run()
        finishLabel.configure(text="Downloaded!")
    except:
        finishLabel.configure(text="Download Error", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percetage_of_completion = bytes_downloaded / total_size * 100
    # print(percetage_of_completion)
    per = str(int(percetage_of_completion))
    pPercentage.configure(text=per + "%")
    pPercentage.update()

    progressBar.set(float(percetage_of_completion) / 100)


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")


app = ctk.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")
app.iconbitmap("YT Dwnld\YDICO.ico")

# label
title = ctk.CTkLabel(
    app, text="Insert a Youtube Link", font=ctk.CTkFont(size=20, weight="bold")
)
title.pack(padx=10, pady=(40,0))

# link input
url_val = tkinter.StringVar()
link = ctk.CTkEntry(app, width=400, height=35, textvariable=url_val)
link.pack(padx=10, pady=(10,0))


# FInish label
finishLabel = ctk.CTkLabel(app, text="")
finishLabel.pack(padx=10, pady=10)


# progress-bar
pPercentage = ctk.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = ctk.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)


optionmenu_var = ctk.StringVar(value="720")
optionmenu = ctk.CTkOptionMenu(
    app,
    values=["360", "480", "720"],
    command=optionmenu_callback,
    variable=optionmenu_var,
)
optionmenu.pack(padx=10, pady=10)

# download button
download_btn = ctk.CTkButton(app, text="Download", command=startdownload)
download_btn.pack(pady=10, padx=10)


em = emoji.emojize("Created with :growing_heart:  @Dev")
author = ctk.CTkLabel(app, text=em, justify=ctk.LEFT, cursor="hand2")
author.pack(pady=10, padx=10)
author.bind(
    "<Button-1>",
    lambda e: webbrowser.open_new_tab(
        "http://www.linkedin.com/in/devendra-singh-08b613254"
    ),
)

app.mainloop()
