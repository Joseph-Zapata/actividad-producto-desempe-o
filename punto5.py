#Realice una FUNCIÓN en Python que calcule el índice de masa corporal de una persona y diga el estado en que se encuentre. Debe recibir los parámetros necesarios.
def calcMasaCorporal(peso, altura):
    altura = altura * altura
    imc = peso/altura
    print("Su IMC es: {0:.2f}".format(imc))
    if(imc<18.5):
        return "Peso insuficiente"
    elif(imc>=18.5 and imc<24.9):
        return "Peso normal"
    elif(imc>=25 and imc<26.9):
        return "Sobrepeso grado I"
    elif(imc>=27 and imc<29.9):
        return "Sobrepeso grado II (Preobesidad)"
    elif(imc>=30 and imc<34.9):
        return "Obesidad de tipo I"
    elif(imc>=35 and imc<39.9):
        return "Obesidad de tipo II"
    elif(imc>=40 and imc<49.9):
        return "Obesidad de tipo III (Mórbida)"
    elif(imc>=50):
        return "Obesidad de tipo IV (Extrema)"

pesoIng = float(input("Ingrese su peso: "))
alturaIng = float(input("Ingrese su altura: "))

print("Usted se encuentra en el grupo: " + calcMasaCorporal(pesoIng, alturaIng))

# Joseph Zapata Piedrahita