#Hacer una actividad que pida al usuario escribir una cantidad X de nombres de personas (puede hacerlo con el ciclo que considere). 
#Después el sistema deberá demostrar cuales son los nombres que empiezan con la letra "C" sea minúscula o mayúscula.
nombres = input("Ingrese los nombres separados por espacios: ").lower().split()
nombres = [x for x in nombres]
cantidad_nombres_c = ""

for i in nombres:
    if(i[0]=="c"):
        cantidad_nombres_c+=(i + " ")
print("Los nombres que empiezan por C o c son: " + cantidad_nombres_c)

# Joseph Zapata Piedrahita