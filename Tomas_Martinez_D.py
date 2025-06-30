totem_autoservicio = {
    "compradores":
    [
        {
            "nombre_comprador": "nombre1",      
        },
        {
            "nombre_comprador": "Nombre2",    # Nombres de comprador "placeholder" para testeo
        }
    ],
    "entradas":
    [
        {
            "stock_entradas_conce": 500,
            "stock_entradas_puente": 1300,
            "stock_entradas_valpo": 100,
            "stock_entradas_vinia": 50
        }
    ]
}

codigo_confirmacion = "Tengoelpoderr42" # Codigo necesario para opción 1 - Compra en Concepción

def verificacion_entero(mensaje:str):
    """Esta funcíon verifica que el input del usuario entregue solamente números.
       La variable "mensaje" sirve para modificar el mensaje que dara el input"""
    while True:
        try:
            numero = int(input(mensaje))
        except ValueError:
            print("\nERROR - Ingrese un valor númerico.")
        else:
            return numero

def verificacion_comprador(nombre:str):
    """Esta función recorre la lista compradores y verifica que el elemento entregado
    (en este caso el nombre de un comprador), no este repetido. En el caso de que se repita entregara False"""
    for i in totem_autoservicio["compradores"]:
        nombre_lista = i["nombre_comprador"]
        if nombre.lower() == nombre_lista.lower():
            return False
        
def verificacion_string(mensaje:str):
    """Esta función verifica que el input del usuario no sea un string vacio"""
    string = input(mensaje)
    if len(string.strip()) < 1:
        print("\nERROR - No puede entregar un texto vacio.")
    else:
        return string


while True:
    print("\nTOTEM AUTOSERVICIO GIRA ROCK AND CHILE IN CHILE")
    print("\n1.- Comprar entrada a “los Fortificados” en Concepción.")  
    print("2.- Comprar entrada a “los Fortificados” en Puente Alto.")  #
    print("3.- Comprar entrada a “los Fortificados” en Muelle Barón en Valparaíso.")  #
    print("4.- Comprar entrada a “los Fortificados” en Muelle Vergara en Viña del Mar.")  #
    print("5.- Salir.")

    opcion = verificacion_entero("\nIngrese su opción: ")

    if opcion == 1: # Concepción
        if totem_autoservicio["entradas"][0]["stock_entradas_conce"] < 1:
            print("No hay entradas disponibles!")
            continue

        print("- Compra en Concepción -")
        nombre_comprador = verificacion_string("Nombre del comprador: ")

        if verificacion_comprador(nombre_comprador) == False:
            print("\nERROR - Ese nombre de comprador ya existe!")
            continue
        else:
            confirmar_codigo = verificacion_string("Código de confirmación: ")

            if confirmar_codigo == codigo_confirmacion:
                comprador_añadir = {"nombre_comprador": nombre_comprador}       # Convertir nombre en diccionario
                totem_autoservicio["compradores"].append(comprador_añadir)      # Añadir comprador a la lista
                totem_autoservicio["entradas"][0]["stock_entradas_conce"] -= 1  # Restar entrada para reflejar compra en el stock
                print(f"Entrada registrada! Stock restante: {totem_autoservicio["entradas"][0]["stock_entradas_conce"]}")
            else:
                print("\nERROR - Código de acceso invalido")

    elif opcion == 2: # Puente Alto
        if totem_autoservicio["entradas"][0]["stock_entradas_puente"] < 1:
            print("No hay entradas disponibles!")
            continue

        print("- Compra en Puente Alto -")
        nombre_comprador = verificacion_string("Nombre del comprador: ")

        if verificacion_comprador(nombre_comprador) == False:
            print("\nERROR - Ese nombre de comprador ya existe!")
            continue
        else:
            numero_entradas = verificacion_entero("Cantidad de entradas (máx 3): ")

            if numero_entradas > 3 or numero_entradas < 1:
                print("ERROR - solo puede comprar entre 1 y 3 entradas por persona")
                continue
            else:
                comprador_añadir = {"nombre_comprador": nombre_comprador}       # Convertir nombre en diccionario
                totem_autoservicio["compradores"].append(comprador_añadir)      # Añadir comprador a la lista
                totem_autoservicio["entradas"][0]["stock_entradas_puente"] -= numero_entradas  # Restar entrada para reflejar compra en el stock
                print(f"Entrada registrada! Stock restante: {totem_autoservicio["entradas"][0]["stock_entradas_puente"]}")

    elif opcion == 3: # Muelle Barón, Valparaíso
        print(f"opcion = {opcion}")
    
    elif opcion == 4: # Muelle Vergara, Viña del Mar
        print(f"opcion = {opcion}")
    
    elif opcion == 5: # Salir
        break

    else:
        print("\nDebe ingresar una opción válida!!")

print("Programa terminado...")