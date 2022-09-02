import boto3
import re
from pathlib import Path
from tkinter import filedialog as fd
from tkinter import *
#Instancio s3 de AWS
s3 = boto3.resource('s3')
#Ventana
window = Tk()
window.geometry("1366x768")
window.configure(bg = "#FFFFFF")
files = [] #array donde guarda los archivos seleccionados
#Funciones
#Leer archivos y listarlos en listbox
def fileread():
    filetype=(
        ('pdf files','*.pdf'),
        ('jpg files','*.jpg'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilenames(filetypes=filetype)
    for item in filename:
        str_files = re.sub('.*?/','',item)
        files.append(item)
        listbox_1.insert("end",str_files)
#Editar nombre de los archivos en el listbox
def edit_text(event):
    #Editar texto
    def accept_edit(event):
        getEntry = entry_edit_listbox.get()
        save_selection = listbox_1.curselection()
        customer = entry_1.get()
        listbox_1.delete(save_selection)
        listbox_1.insert(save_selection,getEntry+customer+'.pdf')
        entry_edit_listbox.destroy()
    #Cancelar Texto
    def cancel_edit(event):
        entry_edit_listbox.destroy()
    #Entry Make
    entry_edit_listbox = Entry(
    width=40,
    bd=0,
    bg="#fff",
    highlightthickness=1,
    font=20
    )
    entry_edit_listbox.place(
        x= 338 + event.x,
        y= 189 + event.y
    )
    entry_edit_listbox.focus_set()
    entry_edit_listbox.bind("<Return>",accept_edit)
    entry_edit_listbox.bind("<Escape>",cancel_edit)
#Subir archivos a un bucket de S3
def uploadfile():
    cont = 0
    customer = entry_1.get()
    selections = listbox_1.get(0,"end")
    for i in selections:
        name_file = re.sub('.*?/','',i)
        file_index = files[cont]
        s3.meta.client.upload_file(file_index, 'dcvcontainer', customer+'/'+name_file)
        cont=+1
    listbox_1.delete(0,"end")
    entry_1.delete(0,"end")
#Cerrar Ventana
def close_window():
    window.destroy()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
#Inicio de Canva
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
#Text Nombre y Apellidos
canvas.create_text(
    338.0,
    83.0,
    anchor="nw",
    text="INTRODUCE NOMBRE Y APELLIDOS",
    fill="#000000",
    font=("Inter ExtraBold", 24 * -1)
)
#Entry Nombre y Apellidos
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    687.0,
    139.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    highlightthickness=0,
    font=40
)
entry_1.place(
    x=337.0,
    y=106.0,
    width=700.0,
    height=64.0
)
#Boton de abrir archivos
button_image_folder = PhotoImage(
    file=relative_to_assets("folder.png"))
button_folder = Button(
    image=button_image_folder,
    borderwidth=0,
    highlightthickness=0,
    command=fileread,
    relief="flat"
)
button_folder.place(
    x=1100.0,
    y=110.0,
    width=50.0,
    height=50.0
)
#Listbox
listbox_image_1 = PhotoImage(
    file=relative_to_assets("listbox_1.png"))
listbox_bg_1 = canvas.create_image(
    687.5,
    419.5,
    image=entry_image_1
)
listbox_1 = Listbox(
    bd=0,
    bg="#D9D9D9",
    selectmode="multiple",
    highlightthickness=0,
    font=20
)
listbox_1.bind(
    "<Double-1>",
    edit_text
)
listbox_1.place(
    x=338.0,
    y=189.0,
    width=699.0,
    height=459.0
)
#Boton de cancelar
button_image_cancel = PhotoImage(
    file=relative_to_assets("button_cancel.png"))
button_cancel = Button(
    image=button_image_cancel,
    borderwidth=0,
    highlightthickness=0,
    command= close_window,
    relief="flat"
)
button_cancel.place(
    x=17.0,
    y=619.0,
    width=212.0,
    height=67.0
)
#Boton de upload
button_image_upload = PhotoImage(
    file=relative_to_assets("button_upload.png"))
button_upload = Button(
    image=button_image_upload,
    borderwidth=0,
    highlightthickness=0,
    command= uploadfile,
    relief="flat"
)
button_upload.place(
    x=1158.0,
    y=619.0,
    width=161.0,
    height=67.0
)
window.resizable(True, True)
window.mainloop()
