import tkinter as tk
import time

def updateclock():
    now_time = time.strftime("%H:%M")
    label1.config(text=now_time)
    label1.after(1000, updateclock)

root = tk.Tk()
root.title("Clock")
root.maxsize(245,245)
root.minsize(200,200)

label1 = tk.Label(root, font=("monospace", 50), fg="white", bg="black")
label1.pack(padx=20, pady=20)

updateclock()

root.mainloop()
