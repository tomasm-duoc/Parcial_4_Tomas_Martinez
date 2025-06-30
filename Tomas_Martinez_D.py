

def verificacion_entero(mensaje:str):
    while True:
        try:
            numero = int(input(mensaje))
        except ValueError:
            print("\nERROR - Ingrese un valor númerico.")
        else:
            return numero


while True:
    print("\nTOTEM AUTOSERVICIO GIRA ROCK AND CHILE IN CHILE")
    print("\n1.- Comprar entrada a “los Fortificados” en Concepción.")
    print("2.- Comprar entrada a “los Fortificados” en Puente Alto.")
    print("3.- Comprar entrada a “los Fortificados” en Muelle Barón en Valparaíso.")
    print("4.- Comprar entrada a “los Fortificados” en Muelle Vergara en Viña del Mar.")
    print("5.- Salir.")

    opcion = verificacion_entero("\nIngrese su opción: ")

    if opcion == 1:
        print(f"opcion = {opcion}")
    
    elif opcion == 2:
        print(f"opcion = {opcion}")
    
    elif opcion == 3:
        print(f"opcion = {opcion}")
    
    elif opcion == 4:
        print(f"opcion = {opcion}")
    
    elif opcion == 5:
        break

    else:
        print("\nDebe ingresar una opción válida!!")

print("Programa terminado...")