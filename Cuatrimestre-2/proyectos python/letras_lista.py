#pedir al usauruo que digite una letra de la a ala z
#y independientemente si puso A en minuscula o mayuscula tiene que hacer que sea igual
#cuente la cantidad de ocurrencias que el usuario digito 

letras = "nnuotfcgsqtwrctjlhrswgbhpshavygyrmtwfrptxwdjgldskninncyfnclamvphqavpxmhzuviaexzovpymlscggsaqawaafhhg"
letra_usu = input("ingrese una letra entre la A y la Z : ").lower()
# 1. pido la letra al usuario y la convierte a minuscula

resultado = letras.count(letra_usu)
#2. cuento cuantas veces aparece la letra en el string
# El "resultado" es la variable donde guardo el numero que devuelve el count
# "letras" es el string donde va a buscar la letra
# ".count" es el metodo con el que cuento cuantas veces aparece algo
# "(letra_usu)" es lo que le digo a .count que busque adentro de letras
print(f"la letra {letra_usu} aparece {resultado} veces en la lista")
