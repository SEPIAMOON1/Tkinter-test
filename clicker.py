import tkinter as tk

def btnclick():
    global clicks
    clicks = clicks + 1
    label1.config(text=f"Clicks: {clicks}")

clicks = 0
root = tk.Tk()
root.title("Clicker Game")
root.maxsize(300,300)
root.minsize(300,300)

label1 = tk.Label(root, font=("Arial", 15), text=f"Clicks: {clicks}")
label1.pack(padx=15, pady=15)

mainbtn = tk.Button(root, font=("Arial", 20), text="Click Me!", border=True, command=btnclick)
mainbtn.pack(padx=30, pady=30)

root.mainloop()
