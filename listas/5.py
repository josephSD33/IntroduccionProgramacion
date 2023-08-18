import tkinter as tt
from tkinter import messagebox

usuarios = {}
Estudiantes = {}
secciones = {}
#Esta funcion da inicio, en ella se muestran las opciones de ingresar o crear un usuario
def inicio():
    global ventana
    ventana = tt.Tk()
    ventana.geometry("300x200")

    tt.Label(ventana, text="Ingreso").pack()
    tt.Button(ventana, text="Ingresar a un usuario", command=ingresar).pack()
    tt.Button(ventana, text="Crear Usuario", command=crear).pack()
    ventana.mainloop()

# La funcion ingresar sirve para introducir el nombre de un usuario existente, guarda el nombre ingresado y le pasa la informacion a la funcion confirmar
def ingresar():
    global ventanaing
    ventanaing = tt.Toplevel(ventana)
    ventanaing.geometry("250x150")
    usuarioing = tt.StringVar()

    tt.Label(ventanaing, text="Ingreso").pack()
    tt.Label(ventanaing, text="Ingrese su usuario").pack()
    tt.Entry(ventanaing, textvariable=usuarioing).pack()
    tt.Button(ventanaing, text="Ingresar", command=lambda: confirmar(usuarioing.get())).pack()
    

# Esta funcion sirve para verficar la informacion del usuario que ah ingresado, verifica el nombre y el rol 
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
    global ventaadmin
    ventaadmin = tt.Toplevel(ventana)
    ventaadmin.geometry("250x150")
    tt.Label(ventaadmin, text="Administrador").pack()

    tt.Button(ventaadmin, text="Crear Sección",command=seccion).pack()
    tt.Button(ventaadmin, text="Consultar Secciones",command=versecciones).pack()
    
   
    
    ventanaing.destroy()
    


def oficinista():
    global ventaofi
    ventaofi = tt.Toplevel(ventana)
    ventaofi.geometry("250x150")
    tt.Label(ventaofi, text="Oficinista").pack()

    tt.Button(ventaofi, text="Inscribir Estudiante",command=inscribirestudiante).pack()
    tt.Button(ventaofi, text="Consultar Secciones",command=versecciones).pack()
    
    ventanaing.destroy()

   

def crear():
    global ventanacrear
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
    ventanacrear.destroy()

def seccion():
    global ventanacrears
    ventanacrears = tt.Toplevel(ventana)
    ventanacrears.geometry("300x200")
    nombreseccion = tt.StringVar()
    cupos = tt.IntVar()

    tt.Label(ventanacrears, text="Crear Nueva Sección").pack()
    tt.Label(ventanacrears, text="Nombre de la sección:").pack()
    tt.Entry(ventanacrears, textvariable=nombreseccion).pack()
    tt.Label(ventanacrears, text="Límite de cupos:").pack()
    tt.Entry(ventanacrears, textvariable=cupos).pack()

    tt.Button(ventanacrears, text="Guardar", command=lambda: guardarseccion(nombreseccion.get(), cupos.get())).pack()

def guardarseccion(nombreseccion, cupos):
    if nombreseccion and cupos > 0:
        if nombreseccion not in secciones:
            Estudiantes[nombreseccion] = []
            secciones[nombreseccion] = cupos
            messagebox.showinfo("Guardado", f"Sección '{nombreseccion}' creada exitosamente.")
            
    else:
        messagebox.showerror("Error", "Debe ingresar un nombre de sección válido y un límite de cupos mayor a cero.")
    ventanacrears.destroy()
    ventaadmin.destroy()
    admin()


def inscribirestudiante():
    global ventanainscribir
    ventanainscribir = tt.Toplevel(ventana)
    ventanainscribir.geometry("400x300")
    nombre = tt.StringVar()
    apellido = tt.StringVar()
    cedula = tt.StringVar()
    seccion_var = tt.StringVar()

    tt.Label(ventanainscribir, text="Inscribir Estudiante").pack()
    tt.Label(ventanainscribir, text="Nombre:").pack()
    tt.Entry(ventanainscribir, textvariable=nombre).pack()
    tt.Label(ventanainscribir, text="Apellido:").pack()
    tt.Entry(ventanainscribir, textvariable=apellido).pack()
    tt.Label(ventanainscribir, text="Cédula:").pack()
    tt.Entry(ventanainscribir, textvariable=cedula).pack()
    tt.Label(ventanainscribir, text="Sección:").pack()
    tt.OptionMenu(ventanainscribir, seccion_var, *secciones).pack()

    tt.Button(ventanainscribir, text="Inscribir", command=lambda: guardarinscripcion(nombre.get(), apellido.get(), cedula.get(), seccion_var.get())).pack()

def guardarinscripcion(nombre, apellido, cedula, seccion):
    if seccion and nombre and apellido and cedula:
        if seccion in secciones:
            if len(Estudiantes[seccion]) < secciones[seccion]:
                estudiante = f"{nombre} {apellido} (Cédula: {cedula})"
                if estudiante not in Estudiantes[seccion]:
                    Estudiantes[seccion].append(estudiante)
                    messagebox.showinfo("Guardado", "Estudiante inscrito exitosamente.")
                else:
                    messagebox.showerror("Error", "Este estudiante ya está inscrito en esta sección.")
            else:
                messagebox.showerror("Error", "Esta sección ha alcanzado su límite de cupos.")
        else:
            messagebox.showerror("Error", "Sección no encontrada.")
    else:
        messagebox.showerror("Error", "Todos los campos deben ser completados.")
    ventanainscribir.destroy()
    oficinista()



def versecciones():
    ventanasecciones = tt.Toplevel(ventana)
    ventanasecciones.geometry("400x300")
    tt.Label(ventanasecciones, text="Secciones y Estudiantes Inscritos").pack()

    for seccion, cupos in secciones.items():
        tt.Label(ventanasecciones, text=f"Sección: {seccion} (Cupos: {cupos})").pack()
        if Estudiantes.get(seccion):
            tt.Label(ventanasecciones, text="Estudiantes Inscritos:").pack()
            for estudiante in Estudiantes[seccion]:
                tt.Label(ventanasecciones, text=estudiante).pack()

    if not secciones:
        tt.Label(ventanasecciones, text="No hay secciones creadas aún.").pack()






inicio()
