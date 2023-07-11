lista=[1,23,2,34,90,43]
mayor= lista[0]
menor=lista[0]
for numero in lista:
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero

print("El número más grande es:", mayor)
print("El número más pequeño es:", menor)