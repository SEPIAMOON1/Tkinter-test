import tkinter as tk

root = tk.Tk()
root.title("First Program")
root.maxsize(400,400)
root.minsize(200,200)

label1 = tk.Label(root, text="Hello, World!", font="Arial")
label1.pack(pady=16)

root.mainloop()
