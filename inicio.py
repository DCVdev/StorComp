from pathlib import Path
import os
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,ttk,font
def password():
    if(input.get()=='123456'):
        os.system("python .\menu.py")
    else:
        print("Contraseña incorrecta")
window = Tk()
window.geometry("704x381")
window.configure(bg = "#FFFFFF")
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    width = 704,
    height = 381,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)
canvas.create_text(
    190.0,
    74.0,
    anchor="nw",
    text="Introduce la contraseña",
    fill="#000000",
    font=("Inter ExtraBold", 24 * -1)
)
style=ttk.Style()
style.configure(
  "MyEntry.TEntry",
    padding=10
)
input=ttk.Entry(style="MyEntry.TEntry",width=20, show="*",
    font=font.Font(
        family="Inter ExtraBold",
        size=14,
        weight=font.BOLD,  
        slant=font.ITALIC
    ))
input.place(x=190,y=125)
btn=ttk.Button(text="Entrar", command=password)
btn.place(x=250,y=180)
window.resizable(False, False)
window.mainloop()
