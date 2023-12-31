import tkinter as tt
from tkinter import messagebox
from tkinter.ttk import *

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
    ventanacrear.geometry("250x150")
    global crearusuario 
    crearusuario = tt.StringVar()
    tt.Label(ventanacrear, text="Crear Usuario Nuevo").pack()
    tt.Label(ventanacrear, text="Nombre del usuario").pack()
    tt.Entry(ventanacrear, textvariable=crearusuario).pack()
    tt.Button(ventanacrear, text="Guardar Usuario", command=guardarusuario).pack()
    ventana.destroy

agendausuario = {}

def guardarusuario():
    usuario = crearusuario.get()
    if usuario:
        agendausuario[usuario] = {
            "contactos": {},
            "tareas": [],
            "eventos": [],
        }
        messagebox.showinfo("Nuevo Usuario Guardado", f"Usuario '{usuario}' ha sido registrado exitosamente.")
       

def accederausuario():
    global ventanaacceso
    ventanaacceso = tt.Toplevel(ventana)
    ventanaacceso.geometry("250x150")
    global nombreIng 
    nombreIng = tt.StringVar()
    tt.Label(ventanaacceso, text="Acceso a Usuario").pack()
    tt.Label(ventanaacceso, text="Ingrese el Usuario").pack()
    tt.Entry(ventanaacceso, textvariable=nombreIng).pack()
    tt.Button(ventanaacceso, text="Ingresar", command=confirmar).pack()

def confirmar():
    usuario = nombreIng.get()
    if usuario in agendausuario:
        ingreso()
    else:
        messagebox.showerror("Error", f"El usuario '{usuario}' no está registrado.")

def ingreso():
    ventanamenu = tt.Toplevel(ventana)
    ventanamenu.geometry("250x150")
    tt.Label(ventanamenu, text="Menu de Usuario").pack()
    tt.Button(ventanamenu, text="Ver Contactos").pack()
    tt.Button(ventanamenu, text="Agregar Contactos",command=agregarcontacto).pack()
    tt.Button(ventanamenu, text="Ver Tareas Pendientes").pack()
    tt.Button(ventanamenu, text="Agregar Tarea").pack()
    tt.Button(ventanamenu, text="Ver Eventos").pack()
    tt.Button(ventanamenu, text="Agregar Evento").pack()


def agregarcontacto():
    usuario = nombreIng.get()
    if usuario in agendausuario:
        ventanac = tt.Toplevel(ventana)
        ventanac.geometry("300x200")
        tt.Label(ventanac, text="Agregar Contacto").pack()

        nombrecontacto = tt.StringVar()
        numerocontacto = tt.StringVar()
        correocontacto = tt.StringVar()

        tt.Label(ventanac, text="Nombre").pack()
        tt.Entry(ventanac, textvariable=nombrecontacto).pack()

        tt.Label(ventanac, text="Número").pack()
        tt.Entry(ventanac, textvariable=numerocontacto).pack()

        tt.Label(ventanac, text="Correo").pack()
        tt.Entry(ventanac, textvariable=correocontacto).pack()

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
                ventanac.destroy()
            else:
                messagebox.showerror("Error", "Por favor, complete todos los campos.")

        tt.Button(ventanac, text="Guardar Contacto", command=guardarcontacto).pack()

    else:
        messagebox.showerror("Error", f"El usuario '{usuario}' no está registrado.")

menuinicio()