frutas = ["sandia", "pera", "uvas", "kiwui", "fresas", "manzana"]
eliminadas = []

def ver_lista():
    print("=" * 80)
    print("Lista de frutas: ", frutas)
    print("=" * 80)
    
def agregar_frutas():
    global frutas
    print("=" * 80)
    nueva_fruta = input("Ingrese una nueva fruta: ").lower()
    if nueva_fruta in frutas:
        print("Esa fruta ya existe en la lista")
    else:
        frutas.append(nueva_fruta)
        print("Fruta agregada correctamente")
    print("=" * 80)
    
def eliminar():
    global frutas, eliminadas
    print("=" * 80)
    print("las opciones para eliminar son: ", frutas)
    while True:
        fruta_eliminar = input("Ingrese la fruta que desea eliminar: ").lower()
        if fruta_eliminar in frutas:
            frutas.remove(fruta_eliminar)
            eliminadas.append(fruta_eliminar)
            print("La fruta eliminada fue: ", fruta_eliminar)
            break
        else:
            print("Esa fruta no existe, intente de nuevo")
    print("=" * 80)

def informe():
    print("=" * 80)
    print("El reporte de las frutas son :")
    print("Total de frutas en la lista ahora: ", len(frutas))
    print("Las frutas en la lista son", frutas)
    print("Total de frutas eliminadas : ", len(eliminadas))
    print("Las frutas eliminadas son : ", eliminadas)
    print("=" * 80)

def actualizar():
    global frutas
    print("=" * 80)
    fruta_actualizar = input("Ingrese la fruta que desea actualizar: ").lower()
    if fruta_actualizar in frutas:
        nueva_fruta = input("Ingrese el nuevo nombre: ").lower()
        posicion = frutas.index(fruta_actualizar)
        frutas[posicion] = nueva_fruta
        print("Fruta actualizada correctamente")
    else:
        print("Esa fruta no existe en la lista")
    print("=" * 80)

opciones = {
    1: ver_lista,
    2: agregar_frutas,
    3: eliminar,
    4: informe,
    5: actualizar,
}

while True:
    print("==== Menu de frutas ====")
    print("opcion 1: Ver lista de frutas")
    print("opcion 2: Agregar una fruta")
    print("opcion 3: Eliminar una fruta")
    print("opcion 4: Informe de frutas")
    print("opcion 5: Actualizar Fruta")
    print("opcion 6: Salir")

    try:
        opcion_menu = int(input("Ingrese una opcion: "))
    except:
        print("Por favor ingrese un numero entero")
        continue

    if opcion_menu == 6:
        break
    elif opcion_menu in opciones:
        opciones[opcion_menu]()
    else:
        print("Opcion no valida")


    
    
    