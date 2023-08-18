import tkinter as tt
from tkinter import messagebox

usuarios = {}
Estudiantes={}
secciones=[]

def inicio():
    global ventana
    ventana = tt.Tk()
    ventana.geometry("300x200")

    tt.Label(ventana, text="Ingreso").pack()
    tt.Button(ventana, text="Ingresar a un usuario",command=ingresar).pack()
    tt.Button(ventana, text="Crear Usuario", command=crear).pack()
    ventana.mainloop()

def ingresar():
    ventanaing= tt.Toplevel(ventana)
    ventanaing.geometry("250x150")
    usuarioing= tt.StringVar

    tt.Label(ventanaing,text="Ingreso").pack()
    tt.Label(ventanaing,text="Ingrese su usuario").pack()
    tt.Entry(ventanaing,textvariable=usuarioing).pack()
    tt.Button(ventanaing,text="Ingresar",command=confirmar).pack()


def confirmar(usuario):
    if usuario in usuarios:
        rol = usuarios[usuario]
        if rol == "administrador":
            admin()
        elif rol == "oficinista":
            oficinista()
        else:
            messagebox.showerror("Error", "Rol desconocido.")
    else:
        messagebox.showerror("Error", "Usuario no encontrado.")
    
     



def admin():
    ventaadmin=tt.Toplevel(ventana)
    ventaadmin.geometry("250x150")
    tt.Label(ventaadmin,text="admin").pack()


def oficinista():
    ventaofi=tt.Toplevel(ventana)
    ventaofi.geometry("250x150")
    tt.Label(ventaofi,text="oficinista").pack()






def crear():
    ventanacrear = tt.Toplevel(ventana)
    ventanacrear.geometry("250x150")
    usuario = tt.StringVar()
    rol = tt.StringVar()

    tt.Label(ventanacrear, text="Crear un nuevo usuario").pack()
    tt.Label(ventanacrear).pack()
    tt.Label(ventanacrear, text="Ingrese el nombre").pack()
    tt.Entry(ventanacrear, textvariable=usuario).pack()
    tt.Label(ventanacrear, text="Ingrese si es administrador u oficinista").pack()
    tt.Entry(ventanacrear, textvariable=rol).pack()

    tt.Button(ventanacrear, text="Guardar", command=lambda: guardarusuario(usuario.get(), rol.get())).pack()

def guardarusuario(usuario, rol):
    usuarios[usuario] = rol
    messagebox.showinfo("Guardado", "Usuario guardado exitosamente.")





inicio()
