#Pide números y mételos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar. Por último, muestra los números ordenados de menor a mayor.
numero = int(input("Ingrese un numero: "))
numerosLista = []
numerosLista.append(numero)

while(numero!=0):
    numero = int(input("Ingrese un numero: "))
    numerosLista.append(numero)

numerosLista.sort()
print(numerosLista)    

# Joseph Zapata Piedrahita