import random
import smtplib
from tkinter import *


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
        accept = Label(otp, text='Successful Verification!', fg='green', font=('Arial', 20))
        accept.place(x=230, y=350)
    else:
        refuse = Label(otp, text='Unsuccessful Verification!', fg='red', font=('Arial', 20))
        refuse.place(x=230, y=350)


otp = Tk()
otp.title('OTP Verification')
otp.geometry('750x400')
otp.config(bg='#00B2EE')


mailMsg = Label(otp, text="E-Mail", justify=LEFT, bg='#00B2EE', font=("Arial", 16))
mailMsg.place(x=15, y=40)

receiverMail = Entry(otp, text='mail.gmail.com', width=35, font=("Arial", 20), borderwidth=0)
receiverMail.place(x=100, y=40)
# receiverM = StringVar()

sendOTP = Button(otp, text="send OTP", width=8, height=1, font=("Arial", 20), borderwidth=0, bg="black", fg="white", command=connectingSender)
sendOTP.place(x=280, y=100)

otpMsg = Label(otp, text="OTP", bg='#00B2EE', font=('Arial', 16))
otpMsg.place(x=15, y=210)

codeEntry = Entry(otp, width=6, font=("Arial", 20), borderwidth=0)
codeEntry.place(x=100, y=210)

verify = Button(otp, text="Verify", width=8, height=1, font=("Arial", 20), borderwidth=0, bg="black", fg="white",
                command=checkOTP)
verify.place(x=280, y=280)

otp.mainloop()