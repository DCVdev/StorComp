from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,Listbox,font
import boto3
import os
s3 = boto3.resource('s3')
def showfiles():
    customer = entry_1.get()
    z = s3.meta.client.list_objects_v2(Bucket='dcvcontainer',Prefix=customer+'/')
    s = z.get('Contents')
    res = [ sub['Key'] for sub in s ]
    for item in res:
        listbox_1.insert("end",item)
def download_all():
    customer = entry_1.get()
    select = listbox_1.get(0,"end")
    os.mkdir('customer/'+customer)
    for element in select:
        s3.meta.client.download_file('dcvcontainer',element,'customer/'+element)
    listbox_1.delete(0,"end")
    entry_1.delete(0,"end")
def download_files():
    customer = entry_1.get()
    select = listbox_1.get("active")
    for i in select:
        print(i)
def close_window():
    window.destroy()
#Creación de ventana
window = Tk()
window.geometry("1366x768")
window.configure(bg = "#FFFFFF")
#Creación de Canvas
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 768,
    width = 1366,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)
#Entry Nombre y Apellidos
canvas.create_rectangle(
    256.0,
    60.0,
    1119.0,
    130.0,
    fill="#000",
    outline=""
)
entry_1= Entry(
    bd=0,
    bg="#D9D9D9",
    highlightthickness=0,
    font=40
)
entry_1.place(
    x=256.0,
    y=60.0,
    width=864.0,
    height=70.0
)
#Boton de listar en listbox
button_image_2 = PhotoImage(
    file="./assets/button_show.png"
    )
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command= showfiles,
    relief="flat"
)
button_2.place(
    x=1157.0,
    y=69.0,
    width=92.0,
    height=53.0
)
#Listbox lista de archivos
listbox_1= Listbox(
    bd=0,
    bg="#D9D9D9",
    selectmode="multiple",
    highlightthickness=0,
    font=20
)
listbox_1.place(
    x=256.0,
    y=140.0,
    height=551,
    width=864.0
)
#Botón de descargar todos los archivos
button_image_download_all = PhotoImage(
    file="./assets/button_download_all.png"
)
btn_download_all = Button(
    image=button_image_download_all,
    borderwidth = 0,
    highlightthickness=0,
    command = download_all,
    relief = "flat"
)
btn_download_all.place(
    x=1157.0,
    y=300.0,
    height=50,
    width=50
)
#Botón de descargar los archivos seleccionados
button_image_download_files = PhotoImage(
    file ="./assets/button_download_files.png"
)
btn_download_files = Button(
    image = button_image_download_files,
    borderwidth = 0,
    highlightthickness = 0,
    command = download_files,
    relief = "flat" 
)
btn_download_files.place(
    x = 1157.0,
    y = 400.0,
    height = 50,
    width = 50
)
#Boton de cerrar ventana
button_image_1 = PhotoImage(
    file="./assets/button_close.png"
    )
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command= close_window,
    relief="flat"
)
button_1.place(
    x=17.0,
    y=619.0,
    width=212.0,
    height=67.0
)
window.resizable(False, False)
window.mainloop()
