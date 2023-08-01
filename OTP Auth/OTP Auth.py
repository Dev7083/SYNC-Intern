import random
import smtplib
import emoji
import webbrowser
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme(
    "blue"
)  # Themes: "blue" (standard), "green", "dark-blue"


def callback(url):
    webbrowser.open_new_tab(url)


def generateOTP():
    randomCode = "".join(str(random.randint(0, 9)) for i in range(6))
    return randomCode


sender = "leilahamada89@gmail.com"
password = "fvypeunocpzhllkz"
code = generateOTP()


def connectingSender():
    receiver = receiverMail.get()
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, password)
    sendingMail(receiver, server)


def sendingMail(receiver, server):
    msg = "Hello! \n This is your OTP is " + code
    server.sendmail(sender, receiver, msg)
    server.quit()


def checkOTP():
    if code == codeEntry.get():
        accept = customtkinter.CTkLabel(app, text="Successful Verification!")

        accept.pack(pady=10, padx=10)
    else:
        refuse = customtkinter.CTkLabel(app, text="Unsuccessful Verification!")

        refuse.pack(pady=10, padx=10)


app = customtkinter.CTk()
app.geometry("400x780")
app.title("OTP Verification")


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

mailMsg = customtkinter.CTkLabel(
    master=frame_1, text="OTP Authentication", justify=customtkinter.LEFT
)
mailMsg.pack(pady=10, padx=10)

receiverMail = customtkinter.CTkEntry(master=frame_1, placeholder_text="Enter Email")
receiverMail.pack(pady=10, padx=10)

sendOTP = customtkinter.CTkButton(
    master=frame_1, text="Send OTP", command=connectingSender
)
sendOTP.pack(pady=10, padx=10)

codeEntry = customtkinter.CTkEntry(master=frame_1, placeholder_text="Enter OTP")
codeEntry.pack(pady=10, padx=10)

verify = customtkinter.CTkButton(master=frame_1, text="Verify OTP", command=checkOTP)
verify.pack(pady=10, padx=10)

emoji = f'{emoji.emojize(":growing_heart:")}'
em = "Created with " + emoji + " @Dev"
author = customtkinter.CTkLabel(
    master=frame_1, text=em, justify=customtkinter.LEFT, cursor="hand2"
)
author.pack(pady=10, padx=10)
author.bind(
    "<Button-1>",
    lambda e: callback("http://www.linkedin.com/in/devendra-singh-08b613254"),
)

app.mainloop()
