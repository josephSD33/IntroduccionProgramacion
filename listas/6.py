def guardar_seccion(nombre_seccion, cupos):
    if nombre_seccion and cupos > 0:
        if nombre_seccion not in secciones:
            secciones.append(nombre_seccion)
            Estudiantes[nombre_seccion] = []
            secciones_cupos[nombre_seccion] = cupos
            messagebox.showinfo("Guardado", f"Sección '{nombre_seccion}' creada exitosamente.")
            ventana.destroy()  # Cerrar la ventana de creación de sección
        else:
            messagebox.showerror("Error", "Esta sección ya existe.")
    else:
        messagebox.showerror("Error", "Debe ingresar un nombre de sección válido y un límite de cupos mayor a cero.")


def crear_seccion():
    ventanacrear = tt.Toplevel(ventana)
    ventanacrear.geometry("300x200")
    nombre_seccion = tt.StringVar()
    cupos = tt.IntVar()

    tt.Label(ventanacrear, text="Crear Nueva Sección").pack()
    tt.Label(ventanacrear, text="Nombre de la sección:").pack()
    tt.Entry(ventanacrear, textvariable=nombre_seccion).pack()
    tt.Label(ventanacrear, text="Límite de cupos:").pack()
    tt.Entry(ventanacrear, textvariable=cupos).pack()

    tt.Button(ventanacrear, text="Guardar", command=lambda: guardar_seccion(nombre_seccion.get(), cupos.get())).pack()

def guardar_seccion(nombre_seccion, cupos):
    if nombre_seccion and cupos > 0:
        if nombre_seccion not in secciones:
            secciones.append(nombre_seccion)
            Estudiantes[nombre_seccion] = []
            secciones_cupos[nombre_seccion] = cupos
            messagebox.showinfo("Guardado", f"Sección '{nombre_seccion}' creada exitosamente.")
        else:
            messagebox.showerror("Error", "Esta sección ya existe.")
    else:
        messagebox.showerror("Error", "Debe ingresar un nombre de sección válido y un límite de cupos mayor a cero.")

#lo elimine