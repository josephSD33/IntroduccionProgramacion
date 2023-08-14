import tkinter as tt
from tkinter import messagebox
from tkinter.ttk import *
agendausuario={}
def menuinicio():
    global ventana
    ventana = tt.Tk()
    ventana.geometry("300x200")
    tt.Label(ventana, text="Menu principal").pack()
    boton1 = tt.Button(ventana, text="Crear un nuevo usuario", command=crear).pack()
    boton2 = tt.Button(ventana, text="Ingresar a un usuario", command=accederausuario).pack()

    ventana.mainloop()

def crear():
    ventanacrear = tt.Toplevel(ventana)
    ventanacrear.geometry("250x200")
    global crearusuario, contrasennausuario
    crearusuario = tt.StringVar()
    contrasennausuario = tt.StringVar()
    tt.Label(ventanacrear, text="Crear Usuario Nuevo").pack()
    tt.Label(ventanacrear, text="Nombre del usuario").pack()
    tt.Entry(ventanacrear, textvariable=crearusuario).pack()
    tt.Label(ventanacrear, text="Contraseña").pack()
    tt.Entry(ventanacrear, textvariable=contrasennausuario, show="*").pack()
    tt.Button(ventanacrear, text="Guardar Usuario", command=guardarusuario).pack()

def guardarusuario():
    usuario = crearusuario.get()
    contrasena = contrasennausuario.get()

    if usuario and contrasena:
        agendausuario[usuario] = {
            "contrasena": contrasena,
            "contactos": {},
            "tareas": [],
            "eventos": [],
        }
        messagebox.showinfo("Nuevo Usuario Guardado", f"Usuario '{usuario}' ha sido registrado exitosamente.")
    else:
        messagebox.showerror("Error", "Por favor, complete todos los campos.")



def accederausuario():
    global ventanaacceso
    ventanaacceso = tt.Toplevel(ventana)
    ventanaacceso.geometry("250x150")
    global nombreIng, contrasenaIng
    nombreIng = tt.StringVar()
    contrasenaIng = tt.StringVar()
    tt.Label(ventanaacceso, text="Acceso a Usuario").pack()
    tt.Label(ventanaacceso, text="Ingrese el Usuario").pack()
    tt.Entry(ventanaacceso, textvariable=nombreIng).pack()
    tt.Label(ventanaacceso, text="Contraseña").pack()
    tt.Entry(ventanaacceso, textvariable=contrasenaIng, show="*").pack()
    tt.Button(ventanaacceso, text="Ingresar", command=confirmar).pack()

def confirmar():
    usuario = nombreIng.get()
    contrasena = contrasenaIng.get()

    if usuario in agendausuario and agendausuario[usuario]["contrasena"] == contrasena:
        ventanaacceso.destroy() 
        ingreso()
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

def ingreso():
    ventanamenu= tt.Toplevel(ventana)
    ventanamenu.geometry("300x250")
    tt.Label(ventanamenu, text="Menu de Usuario").pack()
    tt.Button(ventanamenu, text="Ver Contactos",command=vercontactos).pack()
    tt.Button(ventanamenu, text="Agregar Contactos",command=agregarcontacto).pack()
    tt.Button(ventanamenu, text="Ver Tareas Pendientes").pack()
    tt.Button(ventanamenu, text="Agregar Tarea",command=agregartarea).pack()
    tt.Button(ventanamenu, text="Ver Eventos",command=eventos).pack()
    tt.Button(ventanamenu, text="Agregar Evento",command=agregrarevento).pack()


def agregarcontacto():
    usuario = nombreIng.get()
    if usuario in agendausuario:
        ventanaAc = tt.Toplevel(ventana)
        ventanaAc.geometry("300x200")
        tt.Label(ventanaAc, text="Agregar Contacto").pack()

        nombrecontacto = tt.StringVar()
        numerocontacto = tt.StringVar()
        correocontacto = tt.StringVar()

        tt.Label(ventanaAc, text="Nombre").pack()
        tt.Entry(ventanaAc, textvariable=nombrecontacto).pack()

        tt.Label(ventanaAc, text="Número").pack()
        tt.Entry(ventanaAc, textvariable=numerocontacto).pack()

        tt.Label(ventanaAc, text="Correo").pack()
        tt.Entry(ventanaAc, textvariable=correocontacto).pack()

        def guardarcontacto():
            nombre = nombrecontacto.get()
            numero = numerocontacto.get()
            correo = correocontacto.get()

            if nombre and numero and correo:
                agendausuario[usuario]["contactos"][nombre] = {
                    "numero": numero,
                    "correo": correo
                }
                messagebox.showinfo("Contacto Agregado", f"Contacto '{nombre}' ha sido agregado exitosamente.")
                ventanaAc.destroy()
            else:
                messagebox.showerror("Error", "Por favor, complete todos los campos.")

        tt.Button(ventanaAc, text="Guardar Contacto", command=guardarcontacto).pack()

    else:
        messagebox.showerror("Error", f"El usuario '{usuario}' no está registrado.")

def vercontactos():
    usuario = nombreIng.get()
    if usuario in agendausuario and agendausuario[usuario]["contactos"]:
        ventanavc = tt.Toplevel(ventana)
        ventanavc.geometry("300x200")
        tt.Label(ventanavc, text="Lista de Contactos").pack()
        lista_contactos = agendausuario[usuario]["contactos"]

        for nombre, info in lista_contactos.items():
            tt.Label(ventanavc, text=f"Nombre: {nombre}").pack()
            tt.Label(ventanavc, text=f"Número: {info['numero']}").pack()
            tt.Label(ventanavc, text=f"Correo: {info['correo']}").pack()

    else:
        messagebox.showinfo("Información", "No hay contactos registrados para este usuario.")











#def vertareas():
    
 








def agregartarea():
    usuario= nombreIng.get()
    if usuario in agendausuario:
        ventanaAT= tt.Toplevel(ventana)
        ventanaAT.geometry("300x200")
        tt.Label(ventanaAT,text="Agregar Tarea").pack()
        tareaing=tt.StringVar()
        tt.Label(ventanaAT, text="Descripción").pack()
        tt.Entry(ventanaAT, textvariable=tareaing).pack()

        def guardartarea():
            tarea = tareaing.get()
            if tarea:
                agendausuario[usuario]["tareas"].append(tarea)
                messagebox.showinfo("Tarea Agregada", "Tarea ha sido agregada exitosamente.")
                ventanaAT.destroy()
            else:
                messagebox.showerror("Error", "Por favor, complete la descripción de la tarea.")

        tt.Button(ventanaAT, text="Guardar Tarea", command=guardartarea).pack()

    else:
        messagebox.showerror("Error", f"El usuario '{usuario}' no está registrado.")



    
def eventos():
    usuario = nombreIng.get()
    if usuario in agendausuario and agendausuario[usuario]["eventos"]:
        ventanaev = tt.Toplevel(ventana)
        ventanaev.geometry("300x200")
        tt.Label(ventanaev, text="Eventos").pack()
        lista_eventos = agendausuario[usuario]["eventos"]

        for evento in lista_eventos:
            tt.Label(ventanaev, text=evento).pack()

    else:
        messagebox.showinfo("Información", "No hay eventos registrados para este usuario.")




def agregrarevento():
    usuario = nombreIng.get()
    if usuario in agendausuario:
        ventanae = tt.Toplevel(ventana)
        ventanae.geometry("300x200")
        tt.Label(ventanae, text="Agregar Evento").pack()

        nuevoevento = tt.StringVar()
        nuevafecha = tt.StringVar()

        tt.Label(ventanae, text="Descripción").pack()
        tt.Entry(ventanae, textvariable=nuevoevento).pack()

        tt.Label(ventanae, text="Fecha (dia/mes/año)").pack()
        tt.Entry(ventanae, textvariable=nuevafecha).pack()

        def guardarevento():
            evento = nuevoevento.get()
            fecha = nuevafecha.get()

            if evento and fecha:
                agendausuario[usuario]["eventos"].append(f"Evento: {evento}, Fecha: {fecha}")
                messagebox.showinfo("Evento Agregado", "Evento ha sido agregado exitosamente.")
                ventanae.destroy()
            else:
                messagebox.showerror("Error", "Por favor, complete la descripción y la fecha del evento.")

        tt.Button(ventanae, text="Guardar Evento", command=guardarevento).pack()

    else:
        messagebox.showerror("Error", f"El usuario '{usuario}' no está registrado.")

    

    


menuinicio()