#comentarios de 1 linea
"""comentarios de mas de una linea"""


numero2=input("INTRODUCE TU NUMERO : ")
numero2=int(numero2)
numero = 4
nombre = "Maria"
a,b,c=2,"José",2.3

print(numero2)
print(numero)
print(a)
print(b)
print(c)

suma=numero+numero2
resta=numero2-numero
multiplicacion=numero2*a
division=numero2/c   #division con decimales
division2=numero//c  #division truncada
exponente=numero2**a
modulo=numero2%a

print(suma)
print(resta)
print(multiplicacion)
print(division)
print(division2)
print(exponente)
print(modulo)

"""/////////////////////////////////////////////////////////"""

#String-Cadena


palabra= input("Introduzca su nombre: ")
palabra=str(palabra)

palabra2= input("Introduzac su apellido: ")
palabra2=str(palabra2)


usuario= palabra[0:2]+palabra2[0:5]

usuarioF= usuario+"-SA1"

print("Su nombre de usuario es "+usuarioF)







