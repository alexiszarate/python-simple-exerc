asistencias = int(input("Ingrese cantidad de asistencias: "))

inasistencias = int(input("Ingrese cantidad de inasistencias: "))

porcentaje = int(input("Ingrese cantidad de porcentaje que solicita: "))

total = asistencias + inasistencias

porcentaje = porcentaje * total / 100

calculo1 = asistencias / porcentaje

resultadoPorc = calculo1 * 100

input(resultadoPorc)