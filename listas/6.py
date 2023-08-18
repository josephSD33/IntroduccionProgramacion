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

def inscribir_estudiante():
    ventana_inscribir = tt.Toplevel(ventana)
    ventana_inscribir.geometry("300x200")
    nombre = tt.StringVar()
    apellido = tt.StringVar()
    cedula = tt.StringVar()
    seccion_var = tt.StringVar()

    tt.Label(ventana_inscribir, text="Inscribir Estudiante").pack()
    tt.Label(ventana_inscribir, text="Nombre:").pack()
    tt.Entry(ventana_inscribir, textvariable=nombre).pack()
    tt.Label(ventana_inscribir, text="Apellido:").pack()
    tt.Entry(ventana_inscribir, textvariable=apellido).pack()
    tt.Label(ventana_inscribir, text="Cédula:").pack()
    tt.Entry(ventana_inscribir, textvariable=cedula).pack()
    tt.Label(ventana_inscribir, text="Sección:").pack()
    tt.OptionMenu(ventana_inscribir, seccion_var, *secciones).pack()

    tt.Button(ventana_inscribir, text="Inscribir", command=lambda: guardar_inscripcion(nombre.get(), apellido.get(), cedula.get(), seccion_var.get())).pack()

def guardar_inscripcion(nombre, apellido, cedula, seccion):
    if seccion and nombre and apellido and cedula:
        if seccion in secciones:
            if len(Estudiantes[seccion]) < secciones_cupos[seccion]:
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
