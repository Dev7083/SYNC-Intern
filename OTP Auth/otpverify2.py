import random
import smtplib
# from tkinter import *

import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


def generateOTP():
    randomCode = ''.join(str(random.randint(0, 9)) for i in range(6))
    return randomCode


sender = 'leilahamada89@gmail.com'
password = 'fvypeunocpzhllkz'
code = generateOTP()


def connectingSender():
    receiver = receiverMail.get()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    sendingMail(receiver, server)


def sendingMail(receiver, server):
    msg = 'Hello! \n This is your OTP is ' + code
    server.sendmail(sender, receiver, msg)
    server.quit()


def checkOTP():
    if code == codeEntry.get():
        accept = customtkinter.CTkLabel(app, text='Successful Verification!')
        accept.place(x=300, y=340)
    else:
        refuse = customtkinter.CTkLabel(app, text='Unsuccessful Verification!')
        refuse.place(x=300, y=340)


app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.title('OTP Verification')
app.geometry('750x400')


# # Use CTkButton instead of tkinter Button
# button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
# button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

mailMsg = customtkinter.CTkLabel(app, text="E-Mail", justify=customtkinter.LEFT)
# mailMsg.pack(padx=1, pady=10)
mailMsg.place(x=40, y=40)

receiverMail = customtkinter.CTkEntry(app, placeholder_text='Enter Email', width=500)
receiverMail.place(x=150, y=40)
receiverM = customtkinter.StringVar()

sendOTP = customtkinter.CTkButton(app, text="Send OTP", command=connectingSender)
sendOTP.place(x=300, y=100)
# sendOTP.pack(pady=10, padx=10)

otpMsg = customtkinter.CTkLabel(app, text="OTP")
otpMsg.place(x=40, y=210)

codeEntry = customtkinter.CTkEntry(app,placeholder_text='Enter OTP', width=500)
codeEntry.place(x=150, y=210) 

verify = customtkinter.CTkButton(app, text="Verify", command=checkOTP)
verify.place(x=300, y=280)
app.mainloop()