#preguntarle al usuario que digite un numero 
#con ese numro (10) osea quiere 10 lineas osea el rango
#que opracion quiere hacer + - / * si digita otra cosa que no sea eso
#hacer u a opcion que diga que no es valido 
# que vaya asi 0*0 1*1 2*2 etc hasta el numero que digito el usuario
#en la divison no se puede dividir entre 0 entonces si el usuario digita 0 que diga que no se puede dividir entre 0

Numero_lineas = int(input("Escriba el numero de lienas que desea ver: "))
numero_operacion = input("Escriba la operacion que desea realizar (+, -, *, /): ")

if numero_operacion == "+":
    for i in range(Numero_lineas + 1):
        print(f"El resultado de {i} + {i} = {i+i}")
elif numero_operacion == "-":
    for i in range(Numero_lineas + 1):
        print(f"El resultado de {i} - {i} = {i-i}")
elif numero_operacion == "*":
    for i in range(Numero_lineas + 1):
        print(f"El resultado de {i} * {i} = {i*i}")
elif numero_operacion == "/":
    for i in range(Numero_lineas + 1):
        if i == 0:
            print("No se puede dividir entre 0")
        else:
            print(f"El resultado de {i} / {i} = {i/i}")
else:
    print("Operacion no valida")