lista=[223,2342,12,34,21,6,9,2235,343]
listaM=[]
for numero in lista:
    if numero % 3 == 0:
        listaM.append(numero)

print(listaM)