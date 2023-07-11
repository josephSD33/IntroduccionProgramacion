lista=[1,4,2,9,4,2,1,4,5,1]
pares=0
impares=0
for i,numero in enumerate(lista):
    if i % 2==0:
        pares += numero
    else:
        impares += numero

print(F"la suma de los indice pares es {pares}")       
print(F"la suma de los indices impares es {impares} ")   