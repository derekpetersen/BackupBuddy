import tkinter as tk
import shutil

def on_click():
    source = src.get()
    dest = dst.get()
    shutil.copytree(source,dest)

window = tk.Tk()
window.title("Backup Buddy")
window.geometry("500x300")

top_frame = tk.Frame(window, pady="10")
top_frame.pack()

src_label = tk.Label(top_frame, pady="10", text="Enter the Source")
src_label.pack()

src = tk.Entry(top_frame, width="70")
src.pack()

bottom_frame = tk.Frame(window, pady="10")
bottom_frame.pack()

dst_label = tk.Label(bottom_frame, pady="10", text="Enter the Destination")
dst_label.pack()

dst = tk.Entry(bottom_frame, width="70")
dst.pack()

button_frame = tk.Frame(window, pady="10")
button_frame.pack()

submit = tk.Button(button_frame, text="Submit", command=on_click)
submit.pack()

window.mainloop()

