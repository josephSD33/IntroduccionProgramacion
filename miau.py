import tkinter as tt
from tkinter import messagebox
from tkinter.ttk import *
agendausuario={}
def menuinicio():
    global ventana
    ventana = tt.Tk()
    ventana.geometry("300x200")
    tt.Label(ventana, text="Menu principal",font=("Helvetica", 12),bg="cyan",width="100").pack()
    tt.Label(ventana).pack()
    boton2 = tt.Button(ventana, text="Ingresar a un usuario",width="16",height="2",bg="Gray", command=accederausuario).pack()
    tt.Label(ventana).pack()
    boton1 = tt.Button(ventana, text="Crear un nuevo usuario",width="18",height="2",bg="Gray", command=crear).pack()
    ventana.mainloop()

    

def crear():
    global ventanacrear
    ventanacrear = tt.Toplevel(ventana)
    ventanacrear.geometry("250x200")
    global crearusuario, contrasennausuario
    crearusuario = tt.StringVar()
    contrasennausuario = tt.StringVar()
    tt.Label(ventanacrear,text="Crear un nuevo usuario",font=("Helvetica", 11),bg="cyan",width="100").pack()
    tt.Label(ventanacrear).pack()
    tt.Label(ventanacrear, text="Nombre del usuario",font=("Helvetica", 9),fg="black").pack()
    tt.Entry(ventanacrear, textvariable=crearusuario).pack()
    tt.Label(ventanacrear, text="Contraseña",font=("Helvetica",9),fg="black").pack()
    tt.Entry(ventanacrear,textvariable=contrasennausuario).pack()
    tt.Label(ventanacrear).pack()
    tt.Button(ventanacrear, text="Guardar Usuario",width="12",height="2",bg="Gray", command=guardarusuario).pack()

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
    ventanacrear.destroy()



def accederausuario():
    global ventanaacceso
    ventanaacceso = tt.Toplevel(ventana)
    ventanaacceso.geometry("250x200")
    global nombreIng, contrasenaIng
    nombreIng = tt.StringVar()
    contrasenaIng = tt.StringVar()
    tt.Label(ventanaacceso, text="Acceso a Usuario",font=("Helvetica", 11),bg="cyan",width="100").pack()
    tt.Label(ventanaacceso, text="Ingrese el Usuario").pack()
    tt.Entry(ventanaacceso, textvariable=nombreIng).pack()
    tt.Label(ventanaacceso, text="Contraseña").pack()
    tt.Entry(ventanaacceso, textvariable=contrasenaIng, show="*").pack()
    tt.Label(ventanaacceso).pack()
    tt.Button(ventanaacceso, text="Ingresar",bg="Gray", command=confirmar).pack()

def confirmar():
    usuario = nombreIng.get()
    contrasena = contrasenaIng.get()

    if usuario in agendausuario and agendausuario[usuario]["contrasena"] == contrasena:
        ingreso()
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos.")
    ventanaacceso.destroy() 

def ingreso():
    ventanamenu= tt.Toplevel(ventana)
    ventanamenu.geometry("350x250")
    tt.Label(ventanamenu, text="Menu de Usuario",font=("Helvetica", 13),bg="cyan",width="100").pack()
    tt.Label(ventanamenu).pack()
    tt.Button(ventanamenu, text="Ver Contactos",bg="Gray",command=vercontactos).pack()
    tt.Button(ventanamenu, text="Agregar Contactos",bg="Gray",command=agregarcontacto).pack()
    tt.Label(ventanamenu).pack()
    tt.Button(ventanamenu, text="Ver Tareas Pendientes",bg="Gray",command=vertareas).pack()
    tt.Button(ventanamenu, text="Agregar Tarea",bg="Gray",command=agregartarea).pack()
    tt.Label(ventanamenu).pack()
    tt.Button(ventanamenu, text="Ver Eventos",bg="Gray",command=eventos).pack()
    tt.Button(ventanamenu, text="Agregar Evento",bg="Gray",command=agregrarevento).pack()


def agregarcontacto():
    usuario = nombreIng.get()
    if usuario in agendausuario:
        ventanaAc = tt.Toplevel(ventana)
        ventanaAc.geometry("250x200")
        tt.Label(ventanaAc, text="Agregar Contacto",font=("Helvetica", 11),bg="cyan",width="100").pack()

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

        tt.Button(ventanaAc, text="Guardar Contacto",bg="Gray", command=guardarcontacto).pack()

    else:
        messagebox.showerror("Error", f"El usuario '{usuario}' no está registrado.")

def vercontactos():
    usuario = nombreIng.get()
    if usuario in agendausuario and agendausuario[usuario]["contactos"]:
        ventanavc = tt.Toplevel(ventana)
        ventanavc.geometry("250x200")
        tt.Label(ventanavc, text="Lista de Contactos",font=("Helvetica", 11),bg="cyan",width="100").pack()
        lista_contactos = agendausuario[usuario]["contactos"]

        for nombre, info in lista_contactos.items():
            tt.Label(ventanavc, text=f"Nombre: {nombre}").pack()
            tt.Label(ventanavc, text=f"Número: {info['numero']}").pack()
            tt.Label(ventanavc, text=f"Correo: {info['correo']}").pack()

    else:
        messagebox.showinfo("Información", "No hay contactos registrados para este usuario.")


def vertareas():
    usuario = nombreIng.get()
    if usuario in agendausuario and agendausuario[usuario]["tareas"]:
        ventanavt = tt.Toplevel(ventana)
        ventanavt.geometry("250x200")
        tt.Label(ventanavt, text="Tareas Pendientes",font=("Helvetica", 11),bg="cyan",width="100").pack()
        lista_tareas = agendausuario[usuario]["tareas"]

        for tarea in lista_tareas:
            tt.Label(ventanavt, text=tarea).pack()

    else:
        messagebox.showinfo("Información", "No hay tareas pendientes registradas para este usuario.")


def agregartarea():
    usuario= nombreIng.get()
    if usuario in agendausuario:
        ventanaAT= tt.Toplevel(ventana)
        ventanaAT.geometry("250x200")
        tt.Label(ventanaAT,text="Agregar Tarea",font=("Helvetica", 11),bg="cyan",width="100").pack()
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

        tt.Button(ventanaAT, text="Guardar Tarea",bg="Gray", command=guardartarea).pack()

    else:
        messagebox.showerror("Error", f"El usuario '{usuario}' no está registrado.")



    
def eventos():
    usuario = nombreIng.get()
    if usuario in agendausuario and agendausuario[usuario]["eventos"]:
        ventanaev = tt.Toplevel(ventana)
        ventanaev.geometry("250x200")
        tt.Label(ventanaev, text="Eventos",font=("Helvetica", 11),bg="cyan",width="100").pack()
        lista_eventos = agendausuario[usuario]["eventos"]

        for evento in lista_eventos:
            tt.Label(ventanaev, text=evento).pack()

    else:
        messagebox.showinfo("Información", "No hay eventos registrados para este usuario.")




def agregrarevento():
    usuario = nombreIng.get()
    if usuario in agendausuario:
        ventanae = tt.Toplevel(ventana)
        ventanae.geometry("250x200")
        tt.Label(ventanae, text="Agregar Evento",font=("Helvetica", 11),bg="cyan",width="100").pack()

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
        tt.Label(ventanae).pack()
        tt.Button(ventanae, text="Guardar Evento",bg="Gray", command=guardarevento).pack()

    else:
        messagebox.showerror("Error", f"El usuario '{usuario}' no está registrado.")

    

menuinicio()
