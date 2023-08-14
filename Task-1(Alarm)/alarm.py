import datetime
import time
import winsound
from threading import Thread
import customtkinter as ctk
import webbrowser
import emoji
from time import strftime

# from playsound import playsound

ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.configure(text=time_string)

    app.after(1000, update)


def callback(url):
    webbrowser.open_new_tab(url)


def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        # date = current_time.strftime("%D/%M/%Y")
        # print("The Set Date is:",date)
        # print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
            # winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            sound = [winsound.Beep(600, 900) for i in range(5)]
            print("wAke uP gOizz..")
            # playsound("C:\\Users\\deven\\OneDrive\\Desktop\\SYNC Intern\\camerashutter.wav")
            break


def actual_time():
    set_alarm_timer = f"{hourtime.get()}:{mintime.get()}:{sectime.get()}"
    alarm(set_alarm_timer)


app = ctk.CTk()
app.geometry("400x780")
app.title("Alarm Clock")

# Frame

frame_1 = ctk.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

time_label = ctk.CTkLabel(master=frame_1)
time_label.pack(pady=10, padx=10)

mailMsg = ctk.CTkLabel(master=frame_1, text="Alarm Clock", justify=ctk.LEFT)
mailMsg.pack(pady=10, padx=10)


# hour = ctk.StringVar()
# min = ctk.StringVar()
# sec = ctk.StringVar()

hourtime = ctk.CTkEntry(master=frame_1, placeholder_text="Enter Hour")
hourtime.pack(pady=10, padx=10)
mintime = ctk.CTkEntry(master=frame_1, placeholder_text="Enter Minute")
mintime.pack(pady=10, padx=10)
sectime = ctk.CTkEntry(master=frame_1, placeholder_text="Enter Second")
sectime.pack(pady=10, padx=10)


set_alarm = ctk.CTkButton(
    master=frame_1, text="Set Alarm", command=Thread(target=actual_time).start
)
set_alarm.pack(pady=10, padx=10)

# emoji = f'{emoji.emojize(":growing_heart:")}'
# em = "Created with " + emoji + " @Dev"

em = emoji.emojize("Created with :growing_heart:  @Dev")
author = ctk.CTkLabel(master=frame_1, text=em, justify=ctk.LEFT, cursor="hand2")
author.pack(pady=10, padx=10)
author.bind(
    "<Button-1>",
    lambda e: callback("http://www.linkedin.com/in/devendra-singh-08b613254"),
)

update()
app.mainloop()
