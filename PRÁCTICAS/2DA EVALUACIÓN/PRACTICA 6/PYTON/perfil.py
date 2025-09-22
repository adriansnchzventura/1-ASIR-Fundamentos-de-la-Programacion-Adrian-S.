print("Buenos días, vamos a proceder a hacer su perfil")

p1= input("Introduzca su nombre: ")
p1= str(p1)

p2= input("Introduzca sus Apellidos: ")
p2= str(p2)

p3= input("Introduzca su edad: ")
p3= int(p3)

p4= input("Introduzca su dia y mes de nacimiento (dd-mm): ")
p4= str(p4)

p5= input("Introduzca su pais de residencia: ")
p5= str(p5)

p6= input("Introduzca su Municipio: ")
p6= str(p6)

p7= input("Introduzca su Localidad: ")
p7=str(p7)



print("Generando su perfil . . .")


nombre_completo=p1+p2

user=p1[0:3]+p2[0:4]+p2[9:13]

año=2025-p3

año=str(año)

fecha_nacimiento=p4+"-"+año

lugar=p7+","+p6+"("+p5+")"

print(nombre_completo)
print(user)
print(fecha_nacimiento)
print(lugar)
