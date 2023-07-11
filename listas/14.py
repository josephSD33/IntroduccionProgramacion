tupla=("Joseph","jorge","Ana","Carlos","Jo")
nombres=[]
for nombre in tupla:
    vocales=0
    for letra in nombre:
        if letra in "aeiouAEIOU":
            vocales +=1
        if vocales > 1:
            nombres.append(nombre)   
print(nombres)