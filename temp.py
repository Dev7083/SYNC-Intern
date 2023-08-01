import tkinter as tk
import webbrowser

def callback(url):
    webbrowser.open_new_tab(url)

root = tk.Tk()
root.geometry("300x200")
root.title("Clickable Link")

link = tk.Label(root, text="Click here to visit Google", fg="blue", cursor="hand2")
link.pack()
link.bind("<Button-1>", lambda e: callback("http://www.google.com"))

root.mainloop()
