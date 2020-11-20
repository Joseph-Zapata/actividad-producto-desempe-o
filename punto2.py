#Escribir una función que cuente la cantidad de apariciones de cada carácter en una cadena de texto, y los devuelva en un diccionario.
cadena = input("Escriba su frase: ")
dic = {x:cadena.count(x) for x in cadena} 
print(dic)

# Joseph Zapata Piedrahita