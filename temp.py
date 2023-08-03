# from tkinter import *

import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme(
    "blue"
)  # Themes: blue (default), dark-blue, green


app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.title("OTP Verification")
app.geometry("750x400")

# def optionmenu_callback(choice):
#     print("optionmenu dropdown clicked:", choice)

# optionmenu = customtkinter.CTkOptionMenu(app, values=["option 1", "option 2"],
#                                          command=optionmenu_callback)
# optionmenu.set("option 2")
# optionmenu.pack(padx=10, pady=10)


def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)


optionmenu_var = customtkinter.StringVar(value="option 2")
optionmenu = customtkinter.CTkOptionMenu(
    app,
    values=["option 1", "option 2"],
    command=optionmenu_callback,
    variable=optionmenu_var,
)
optionmenu.pack()


# def combobox_callback(choice):
#     print("combobox dropdown clicked:", choice)

# combobox = customtkinter.CTkComboBox(app, values=["option 1", "option 2"],
#                                      command=combobox_callback)
# combobox.set("option 2")
# combobox.pack(padx=10, pady=10)


# # Use CTkButton instead of tkinter Button
# button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
# button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

# mailMsg = customtkinter.CTkLabel(app, text="E-Mail", justify=customtkinter.LEFT)
# # mailMsg.pack(padx=1, pady=10)
# mailMsg.place(x=40, y=40)

# receiverMail = customtkinter.CTkEntry(app, placeholder_text='Enter Email', width=500)
# receiverMail.place(x=150, y=40)
# receiverM = customtkinter.StringVar()

# sendOTP = customtkinter.CTkButton(app, text="Send OTP")
# sendOTP.place(x=300, y=100)
# # sendOTP.pack(pady=10, padx=10)

# otpMsg = customtkinter.CTkLabel(app, text="OTP")
# otpMsg.place(x=40, y=210)

# codeEntry = customtkinter.CTkEntry(app,placeholder_text='Enter OTP', width=500)
# codeEntry.place(x=150, y=210)

verify = customtkinter.CTkButton(app, text="Verify")
verify.place(x=300, y=280)


app.mainloop()
