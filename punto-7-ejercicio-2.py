num1 = int(input("¿Dime el primer número?"))
num2 = int(input("¿Dime el segundo número?"))

resultadoPos = num1 + num2
resultadoNeg = num1 - num2
resultadoMul = num1 * num2
resultadoDiv = num1 / num2
resultadoPot = pow(num1, num2) 

print("La suma de ambos numeros es:", resultadoPos)
print("La resta del primer numero sobre el segundo es:", resultadoNeg)
print("La multiplicacion de ambos numeros es:", resultadoMul)
print("La division del primer numero sobre el segundo es:", resultadoDiv)
print("La potencia del primer numero elevado al segundo es:", resultadoPot)