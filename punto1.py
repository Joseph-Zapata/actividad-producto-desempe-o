#Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad de apariciones de cada palabra en la cadena. 
cadena = input("Escriba su frase: ").split()
dic = {x:cadena.count(x) for x in cadena} 
print(dic)

# Joseph Zapata Piedrahita