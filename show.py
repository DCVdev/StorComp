from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,Listbox,font,Scrollbar,Label
import boto3
import os,re
s3 = boto3.resource('s3')
search = []#Array donde se guarda la busqueda
def showfiles():
    customer = entry_1.get()
    zs = s3.meta.client.list_objects_v2(Bucket='dcvcontainer')
    #z = s3.meta.client.list_objects_v2(Bucket='dcvcontainer',Prefix=customer+'/')
    s = zs.get('Contents')
    res = [ sub['Key'] for sub in s ]
    searching = [match for match in res if customer in match]
    for item in searching:
        listbox_1.insert("end",item)
#Mostrar mensaje
def mostrar_mensaje():
    msn_text = Label(
        text="archivos descargados",
        font="30"
    )
    msn_text.place(
        x=550,
        y=700
    )
    window.after(3000, lambda: msn_text.destroy())
#Descargar todos los archivos
def download_all():
    customer = entry_1.get()
    select = listbox_1.get(0,"end")
    for element in select:
        #str_files = re.sub('.*?/','',element)
        str_files_principal = re.sub('/.*?','',element)
        s3.meta.client.download_file('dcvcontainer',element,str_files_principal)
    mostrar_mensaje()
#Descargar los archivos seleccionados
def download_files():
    customer = entry_1.get()
    select = [listbox_1.get(i) for i in listbox_1.curselection()]
    for selections in select:
        #str_files = re.sub('.*?/','',selections)
        str_files_principal = re.sub('/.*?','',selections)
        s3.meta.client.download_file('dcvcontainer',selections,str_files_principal)
    mostrar_mensaje()
#Limpiar todo
def clean_all():
    listbox_1.delete(0,"end")
    entry_1.delete(0,"end")
#Cerrar ventana
def cerrar_ventana():
    window.destroy()
#Creación de ventana
window = Tk()
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry("%dx%d+0+0" % (w, h))
window.configure(bg = "#FFFFFF")
#Creación de Canvas
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
    window,
    bd=0,
    bg="#D9D9D9",
    selectmode="multiple",
    highlightthickness=0,
    font=20,
)
listbox_1.place(
    x=256.0,
    y=140.0,
    height=551,
    width=864.0
)
#Scrollbar
scroll = Scrollbar(
    orient="vertical",
    bd=2
)
scroll.place(
    x=1110,
    y=140,
    height=551
)
#Configuración de la posición de listbox con scrollbar
listbox_1.config(yscrollcommand = scroll.set)
scroll.config(command = listbox_1.yview)
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
#Boton de limpiar todo
button_image_clean = PhotoImage(
    file="./assets/button_clean.png"
)
button_clean = Button(
    image=button_image_clean,
    borderwidth=0,
    highlightthickness=0,
    command=clean_all,
    relief="flat"
)
button_clean.place(
    x=1157.0,
    y=500,
    height=50,
    width=50
)
#Boton de cerrar ventana
button_image_1 = PhotoImage(
    file="./assets/button_close.png"
    )
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=cerrar_ventana,
    relief="flat"
)
button_1.place(
    x=17.0,
    y=719.0,
    width=212.0,
    height=67.0
)
window.resizable(False, False)
window.mainloop()