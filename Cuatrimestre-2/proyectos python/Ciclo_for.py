colores = ["rojo", "azul", "verde", "amarillo", "naranja"]

for color in  colores:
    print(f"El color es: {color}")
    
print("\n")


precios = [1500, 2300, 800, 4200, 650]

for i in range(len(precios)):
    print(f"El precio del producto {i+1} es: {precios[i]}")
    
print("\n")


for i in range(len(precios)):
    if precios[i] > 3000:
        print(f"El producto {i+1} es caro con un precio de: {precios[i]}")
    else:
        print(f"El producto {i+1} es barato con un precio de: {precios[i]}")