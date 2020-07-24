#Additive Congruential Random Number Generator
#ACORN (PRNG)
#Universidad del Valle de Guatemala
#Grupo 7 Cifrado de información

#Referencia de implementación de código
#https://www.geeksforgeeks.org/additive-congruence-method-for-generating-pseudo-random-numbers/

#Definimos nuestra función ACORN
#Recibe como parámetros x0 x inicial,m modulo y c un valor entre 0 y m.
#numberOfRN cantidad de números
#Retorna los randomNumbers
def additiveCongruentialMethod(x0,m,c,numberOfRN):
    randomNumbers=[]
    #En el indice 0 se encuentra la semilla
    randomNumbers.append(x0)
    #Se genera el siguiente valor a partir del anterior + c en modulo m
    for i in range(1,numberOfRN):
        randomNumbers.append((randomNumbers[i-1]+c)%m)
    #Se retorna la lista con los valores pseudo random
    return randomNumbers



#Es muy fácil de implementar y fácil de descrifrar al ver el patrón que se sigue
m=20
x0=5
c=11
rnQuantity=20
#Esto genera números random entre 0 y 20.
randomNumbers=additiveCongruentialMethod(x0,m,c,rnQuantity)
print("Los números random generados fueron los siguientes:" )
for rn in randomNumbers:
    print(rn)