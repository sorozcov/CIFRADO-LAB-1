#Descifrando el siguiente estado de un Linear Congruential Generators
#Conociendo el estado anterior
from sympy import mod_inverse

print("Parte A")
s3 = 2148910388216139
m = 915451635481687
c = 5886893188886454 
n = 6108133789056532 
#Al tener s3,m,c y n solamente calculamos el siguiente termino con la formula
print("S4")
print((s3*m+c)%n)

print("Parte B")
#Al tener s1 y 2, m y n.
#Calculamos c despejando para el valor con los valores S1 Y S2
#Luego usamos el valor C para la parte general
s1 = 1526203935246140
s2 = 1251340539300040
m = 7544713835650436
n = 3059121001727213
print("C")
c = n*m+s2 - s1*3
print(c)
print("S3")
print((s2*m+c)%n)






