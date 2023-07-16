listaCorreos={}
while True :
    nombre= input("Ingrese el nombre de la persona o escriba salir para terminar: ")
    if nombre.lower()== "terminar":
        break
    correo= input(F"Ingrese el correo electronico de {nombre} :")
        
    listaCorreos[nombre]= correo

print("Su lista de correos es")
print(listaCorreos)



