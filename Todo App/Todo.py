import customtkinter as ctk



def add_todo():
    todo = entry.get()
    label = ctk.CTkLabel(scrollable_frame, text=todo)
    label.pack()
    entry.delete(0, ctk.END)


# root widjet
root=ctk.CTk()
root.geometry("750x450")
root.title("Todo App")


title_label = ctk.CTkLabel(root, text="Daily Tasks", font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=10, pady=(40,20))

scrollable_frame = ctk.CTkScrollableFrame(root, width=500, height=200)
scrollable_frame.pack()

entry = ctk.CTkEntry(scrollable_frame, placeholder_text="Add todo")
entry.pack(fill="x")

button = ctk.CTkButton(root, text="Add", width=500, command=add_todo)
button.pack(pady=20)

root.mainloop()