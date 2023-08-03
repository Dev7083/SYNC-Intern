# import tkinter
import customtkinter as ctk
from pytube import YouTube
import os
import emoji
import webbrowser

# location for downloading
DOWNLOAD_FOLDER = f"{os.getenv('USERPROFILE')}\\Downloads"
# CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
## DOWNLOADS_DIRECTORY = os.path.join(CURRENT_DIRECTORY, "Downloads")


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")


app = ctk.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")
# app.iconbitmap("YT Dwnld\YDICO.ico")


def startdownload():
    choice = optionmenu.get()
    ytLink = link.get()
    if choice == choices[0]:
        try:
            ytObject = YouTube(ytLink, on_progress_callback=on_progress)
            title.configure(text=ytObject.title, text_color="white")
            # video = ytObject.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            video = ytObject.streams.filter(res="720p", progressive=True).first()
            finishLabel.configure(text="")
            video.download(DOWNLOAD_FOLDER)
            finishLabel.configure(text="Downloaded!")
        except:
            finishLabel.configure(text="Download Error", text_color="red")
    elif choice == choices[1]:
        try:
            ytObject = YouTube(ytLink, on_progress_callback=on_progress)
            title.configure(text=ytObject.title, text_color="white")
            # video = ytObject.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            video = ytObject.streams.filter(res="720p", progressive=True).first()
            finishLabel.configure(text="")
            video.download(DOWNLOAD_FOLDER)
            finishLabel.configure(text="Downloaded!")
        except:
            finishLabel.configure(text="Download Error", text_color="red")

    elif choice == choices[2]:
        try:
            ytObject = YouTube(ytLink, on_progress_callback=on_progress)
            title.configure(text=ytObject.title, text_color="white")
            # video = ytObject.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            video = ytObject.streams.filter(res="360p", progressive=True).first()
            finishLabel.configure(text="")
            video.download(DOWNLOAD_FOLDER)
            finishLabel.configure(text="Downloaded!")
        except:
            finishLabel.configure(text="Download Error", text_color="red")
    elif choice == choices[3]:
        try:
            ytObject = YouTube(ytLink, on_progress_callback=on_progress)
            title.configure(text=ytObject.title, text_color="white")
            # audio = ytObject.streams.get_audio_only()
            audio = ytObject.streams.filter(abr="160kbps", progressive=False).first()
            finishLabel.configure(text="")
            audio.download(DOWNLOAD_FOLDER, filename=ytObject.title + ".mp3")
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


# label
title = ctk.CTkLabel(
    app, text="Insert a Youtube Link", font=ctk.CTkFont(size=20, weight="bold")
)
title.pack(padx=10, pady=(40, 0))

# link input
url_val = ctk.StringVar()
link = ctk.CTkEntry(app, width=400, height=35, textvariable=url_val)
link.pack(padx=10, pady=(10, 0))


# FInish label
finishLabel = ctk.CTkLabel(app, text="")
finishLabel.pack(padx=10, pady=10)


# progress-bar
pPercentage = ctk.CTkLabel(app, text="0%")
pPercentage.pack()


progressBar = ctk.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)


# optionmenu_var = ctk.StringVar(value="720")
choices = ["720", "480", "360", "Audio"]
optionmenu = ctk.CTkOptionMenu(app, values=choices)
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
