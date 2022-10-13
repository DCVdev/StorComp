from pathlib import Path
import os
from tkinter import *
window = Tk()
window.geometry("1375x795")
window.configure(bg = "#FFFFFF")
#Abrir ventana de descargar archivos
def abrir_show():
    os.system("python .\show.py")
#Abrir ventana de subir archivos
def abrir_upload():
    os.system("python .\\upload.py")
#Cerrar sesion
def cerrar_ventana():
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

btn_upload= Button(text="SUBIR ARCHIVOS",bd=5,relief="groove",state="normal",font=20, command = abrir_upload)
btn_upload.place(
    x=341,
    y=108,
    height=75,
    width=680
)
btn_show= Button(text="DESCARGAR ARCHIVOS",bd=5,relief="groove",state="normal",font=20, command = abrir_show)
btn_show.place(
    x=341,
    y=238,
    height=75,
    width=680
    )
btn_close= Button(text="CERRAR SESION",bd=5,relief="groove",state="normal",font=20, command = cerrar_ventana)
btn_close.place(
    x=341,
    y=398,
    height=75,
    width=680
)
window.resizable(False, False)
window.mainloop()
