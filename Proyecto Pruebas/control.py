#usuario
agenda = {}
#opciones para usuario 
while True:
    print("\n--- AGENDA ---")
    print("1. Crear nuevo usuario")
    print("2. Acceder a un usuario existente")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ").strip()
    import os 
    os.system("cls")
    if opcion == "1":
        usuario = input("Ingrese el nombre del nuevo usuario: ").strip()
        agenda[usuario] = {
            "contactos": {},
            "tareas": [],
            "eventos": [],
            "correos": {}
        }
        print(F"Usuario {usuario} fue creado")
    
    elif opcion=="2":
        usuario= input("Ingrese en nombre del usuario").strip()
        
        if usuario in agenda:
             while True:
                print("\n--- MENÚ DE USUARIO ---")
                print("1. Ver contactos")
                print("2. Agregar contacto")
                print("3. Ver tareas pendientes")
                print("4. Agregar tarea")
                print("5. Ver eventos")
                print("6. Agregar evento")
                print("7. Volver a las opciones de usuario")
               
                
                eleccionMenu= input("Selecione una opcion del menu: ").strip()
                os.system("cls")
                if eleccionMenu == "1":
                    contactos = agenda[usuario]["contactos"]
                    if len(contactos) == 0:
                        print("No hay contactos registrados.")
                    else:
                        print("--- CONTACTOS ---")
                        for nombre, detalles in contactos.items():
                            print("Nombre: {}".format(nombre))
                            print("Teléfono: {}".format(detalles['telefono']))
                            print("Correo: {}".format(detalles['correo']))

                elif eleccionMenu == "2":
                    nombrecontacto = input("Ingrese el nombre del contacto: ").strip()
                    telefono = input("Ingrese el número de teléfono: ").strip()
                    correo = input("Ingrese el correo electrónico: ").strip()
                    
                    agenda[usuario]['contactos'][nombrecontacto] = {
                        'telefono': telefono,
                        'correo': correo
                    }
                    
                    print(F"Contacto '{nombrecontacto}' agregado exitosamente.")

                elif eleccionMenu == "3":
                    tareas = agenda[usuario]['tareas']
                    if len(tareas) == 0:
                        print("No hay tareas pendientes.")
                    else:
                        print("--- TAREAS PENDIENTES ---")
                        for tarea in tareas:
                            print(f"- {tarea}")

                elif eleccionMenu == "4":
                    tarea = input("Ingrese la tarea pendiente: ").strip()
                    agenda[usuario]['tareas'].append(tarea)
                    print("Tarea pendiente agregada exitosamente.")

                elif eleccionMenu == "5":
                    eventos = agenda[usuario]['eventos']
                    if len(eventos) == 0:
                        print("No hay eventos programados.")
                    else:
                        print("--- EVENTOS ---")
                        for evento in eventos:
                            print(f"- {evento}")

                elif eleccionMenu == "6":
                    evento = input("Ingrese el evento: ").strip()
                    agenda[usuario]['eventos'].append(evento)
                    print("Evento agregado exitosamente.")

                elif eleccionMenu == "7":
                     break
                else:
                    print("Opción inválida. Intente nuevamente.") 
        else:
            print("Usuario no encontrado. Por favor, cree un nuevo usuario.")
    elif opcion =="3":
        break
    
    else:
        print("Opción inválida. Intente nuevamente.")
    
