frase = "mifrasefavorita"
#la cantidad de vocales que hay sin repetir y cuales son distintas 
vocales = "aeiou" #identifico las vocales 
vocales_frase = set()

for letras in frase:
    if letras in vocales:
        vocales_frase.add(letras)


print("=" * 120)
print(f"la cantidad de vocales que hay en la frase son {len(vocales_frase)} y las vocales que hay en la frase son {vocales_frase} ")
print("=" * 120)

print(" ")
print("_" * 150)

# Notas de estudiantes la primera de los examenes 1, la 2 de los examenes 2 y la 3 del examen 3
#lista del nombre del estudiante

examen1 = [72, 45, 76, 70, 99, 98, 53, 59, 57, 98]
examen2 = [45, 75, 95, 93, 53, 90, 55, 55, 51, 83]
examen3 = [55, 58, 97, 99, 92, 68, 46, 96, 78, 78]
estudiantes = ["CRISTIAN", "DANIEL", "SHARON", "STEVEN", "JOSE", "ANDERSON", "GENIFER","JUAN DIEGO", "SEBASTIAN","JOHAN"]


#nota 1 estudiante 1
#un programa que le diga cada estudiante como le fue en cada examen
#si es menor a 65 reprobado mayor aprobado y promedio 
for i in range(len(examen1)):
    promedio = round((examen1[i] + examen2[i] + examen3[i]) / 3, 2)
    print("=" * 120)
    print(f"El nombre del estudiante es : {estudiantes[i]}")
    print(f"La nota del primero examen fue : {examen1[i]}")
    print(f"La nota del segundo examen fue : {examen2[i]}")
    print(f"La nota del tercer examen fue : {examen3[i]}")
    print(f"El promedio del estudiante fue : {promedio}")
    if promedio < 65:
        print(f"El estudiante tuvo un promedio de {promedio} esta reprobado!!")
    else :
        print(f"El estudiante tuvo un promedio de {promedio} fue aprobado!!")
    print("=" * 120)

print(" ")
print("_" * 150)


examen1 = [72, 45, 76, 70, 99, 98, 53, 59, 57, 98]
examen2 = [45, 75, 95, 93, 53, 90, 55, 55, 51, 83]
examen3 = [55, 58, 97, 99, 92, 68, 46, 96, 78, 78]
estudiantes = ["CRISTIAN", "DANIEL", "SHARON", "STEVEN", "JOSE", "ANDERSON", "GENIFER","JUAN DIEGO", "SEBASTIAN","JOHAN"]

print(f"{'Estudiante':<12} {'Examen 1':<10} {'Examen 2':<10} {'Examen 3':<10} {'Promedio':<10} {'Resultado':<10}")
print("=" * 65)

for i in range(len(examen1)):
    promedio = round((examen1[i] + examen2[i] + examen3[i]) / 3, 2)
    resultado = "Reprobado" if promedio < 65 else "Aprobado"
    print(f"{estudiantes[i]:<12} {examen1[i]:<10} {examen2[i]:<10} {examen3[i]:<10} {promedio:<10} {resultado:<10}")
    

print("*" * 80)
print("\t" * 3,"BIENVENIDO AL PROGRAMA")
print("\t" * 2,"NOTAS ESTUDIANTE PROGRAMACIÓN 1 UNIVERSIDAD CENTRAL")
print("*" * 80)

estudiantes = ["CRISTIAN", "DANIEL", "SHARON", "STEVEN", "JOSE", "ANDERSON", "GENIFER","JUAN DIEGO", "SEBASTIAN","JOHAN"]
notas_exa_uno = [72, 45, 76, 70, 99, 98, 53, 59, 57, 98]
notas_exa_dos = [45, 75, 95, 93, 53, 90, 55, 55, 51, 83]
notas_exa_tres = [55, 58, 97, 99, 92, 68, 46, 96, 78, 78]
estudiantes_aprobados = 0

#ENCABEZADO
print(f"{'Estudiante':<10} {'Examen 1':<10} {'Examen 2':<10} {'Examen 3':<10} {'Promedio Final':<15} {'Resultado':<15}")

for indice in range(len(estudiantes)):

    nombre_estudiante = estudiantes[indice]

    nota_primer_examen = notas_exa_uno[indice]
    nota_segundo_examen = notas_exa_dos[indice]
    nota_tercer_examen = notas_exa_tres[indice]

    promedio = (nota_primer_examen + nota_segundo_examen + nota_tercer_examen) / 3
    resultado = "APROBADO" if promedio >= 70 else "REPROBADO"

    if resultado == "APROBADO":
        estudiantes_aprobados += 1

    print(f"{nombre_estudiante:<10} {nota_primer_examen: <10} {nota_segundo_examen: <10} {nota_tercer_examen: <10} {50: <15} {resultado}")


cantidad_estudiantes = len(estudiantes)
print(f"Rendimiento del curso de programación I. Total de estudiantes {cantidad_estudiantes} | porcentaje de aprobacion: {estudiantes_aprobados / cantidad_estudiantes *100 }")
 