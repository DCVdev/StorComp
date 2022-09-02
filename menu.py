import runpy
from pathlib import Path
import os
from tkinter import *
window = Tk()
window.geometry("1375x795")
window.configure(bg = "#FFFFFF")
def abrir_show():
    os.system("python .\show.py")
def abrir_upload():
    os.system("python .\\upload.py")
def close_window():
    window.destroy()
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 795,
    width = 1375,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    341.0,
    108.0,
    1024.0,
    185.0,
    fill="#D9D9D9",
    outline="")
canvas.create_text(
    564.0,
    127.0,
    anchor="nw",
    text="SUBIR ARCHIVOS",
    fill="#000000",
    font=("Inter ExtraBold", 24 * -1)
)
btn= Button(text="SUBIR ARCHIVOS", command = abrir_upload)
btn.place(x=341,y=108)
canvas.create_rectangle(
    341.0,
    242.0,
    1024.0,
    319.0,
    fill="#D9D9D9",
    outline="")
canvas.create_text(
    531.0,
    264.0,
    anchor="nw",
    text="VER ARCHIVOS",
    fill="#000000",
    font=("Inter ExtraBold", 24 * -1)
)
btn= Button(text="DESCARGAR ARCHIVOS", command = abrir_show)
btn.place(x=341,y=242)
canvas.create_rectangle(
    346.0,
    398.0,
    1029.0,
    475.0,
    fill="#D9D9D9",
    outline=""
)
canvas.create_text(
    579.0,
    417.0,
    anchor="nw",
    text="CERRAR SESION",
    fill="#000000",
    font=("Inter ExtraBold", 24 * -1)
)
btn= Button(text="CERRAR SESION", command = close_window)
btn.place(x=341,y=398)
window.resizable(False, False)
window.mainloop()
