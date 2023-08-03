# import ffmpeg
# ffmpeg_audio = ffmpeg.input('audio.mp3')
# ffmpeg_video = ffmpeg.input('video.mp4')
# ffmpeg.output(ffmpeg_audio, ffmpeg_video, "finished_video.mp4").run(overwrite_output=True)
# # ffmpeg.concat(ffmpeg_audio, ffmpeg_video, v=1, a=1).output('finished_video.mp4').run()

import tkinter as tk
import customtkinter as ctk
root = ctk.CTk()
root.withdraw()

entry = ctk.CTkEntry(root)
entry.pack()

entry.insert(0, root.clipboard_get())

root.mainloop()
