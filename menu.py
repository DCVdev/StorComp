from pathlib import Path
import os
from tkinter import *
#
#  Crea la ventana y le añado propiedades
#
window = Tk()
window.geometry("1375x795")
window.configure(bg = "#FFFFFF")
#
# Abre el archivo show.py
#
def abrir_show():
    os.system("python .\show.py")
#    
# Abre el archivo upload.py
#
def abrir_upload():
    os.system("python .\\upload.py")
#    
# Cierra la ventana
#
def cerrar_ventana():
    window.destroy()
#
# Añade contenido a la ventana
#
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
#
# Crea boton que llama a abrir_upload
#
btn_upload= Button(text="SUBIR ARCHIVOS",bd=5,relief="groove",state="normal",font=20, command = abrir_upload)
btn_upload.place(
    x=341,
    y=108,
    height=75,
    width=680
)
#
# Crea boton que llama a abrir_show
#
btn_show= Button(text="DESCARGAR ARCHIVOS",bd=5,relief="groove",state="normal",font=20, command = abrir_show)
btn_show.place(
    x=341,
    y=238,
    height=75,
    width=680
    )
#
# Crea boton que llama a cerrar_ventana
#
btn_close= Button(text="CERRAR SESION",bd=5,relief="groove",state="normal",font=20, command = cerrar_ventana)
btn_close.place(
    x=341,
    y=398,
    height=75,
    width=680
)
window.resizable(False, False)#Evita que se pueda modificar el tamaño de la ventana
window.mainloop()
