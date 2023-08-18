import tkinter as tt
from tkinter import messagebox


usuarios = {}
def inicio():
   global ventana
   ventana = tt.Tk()
   ventana.geometry("300x200")
   

   tt.Label(ventana, text="Menu de ingreso").pack()

   tt.Button(ventana, text="Crear Usuario", command=crear_ventana_ingreso).pack()


   tt.Button(ventana, text="Acceder a Usuario").pack()


   ventana.mainloop()

def crear_ventana_ingreso():
    ventana_ingreso = tk.Toplevel(ventana)
    ventana_ingreso.title("Crear Usuario")

    nombre_label = tk.Label(ventana_ingreso, text="Nombre de Usuario:")
    nombre_label.pack()

    nombre_entry = tk.Entry(ventana_ingreso)
    nombre_entry.pack()

    tipo_label = tk.Label(ventana_ingreso, text="Elige el tipo de usuario:")
    tipo_label.pack()

    administrador_button = tk.Button(ventana_ingreso, text="Administrador", command=lambda: guardar_informacion(nombre_entry.get(), "Administrador"))
    administrador_button.pack()

    oficinista_button = tk.Button(ventana_ingreso, text="Oficinista", command=lambda: guardar_informacion(nombre_entry.get(), "Oficinista"))
    oficinista_button.pack()


def guardar_informacion(nombre, tipo_usuario):
    usuarios[nombre] = tipo_usuario
    messagebox.showinfo("Información Guardada", f"Usuario {nombre} creado y guardado como {tipo_usuario}.")




inicio()