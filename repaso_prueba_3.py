turistas = {"001": ["John Doe", "Estados Unidos", "12-01-2024"],
            "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
            "012": ["Julian Martinez", "Argentina", "19-09-2023"],
            "014": ["Agustin Morales", "Argentina", "28-03-2024"],
            "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
            "006": ["Maria Lopez", "Mexico", "08-12-2023"],
            "007": ["Joao Silva", "Brasil", "20-06-2024"],
	        "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
	        "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
            "008": ["Ana Santos", "Brasil", "03-10-2023"],
            "010": ["Martin Fernandez", "Argentina", "13-03-2023"],
            "011": ["Sofia Gomez", "Argentina", "07-04-2024"],
     }

def turista_por_pais(pais):
    nombre_turista= []
    for key in turistas:
        if turistas[key][1] == pais:
            nombre_turista.append(turistas[key][0])
    if len(nombre_turista) == 0:
        print ("No hay turistas en este pais.")
    else:
        for nombre in nombre_turista:
            print (f"Nombre del turista: {nombre}")
            
def turista_por_eliminar(eliminar):
    eliminar_turistas=[]
    for key,datos in turistas.items():
        if datos[0].lower() == eliminar.lower():
            eliminar_turistas.append(key)
    if not eliminar_turistas:
        print("No se encontro al turista con el nombre:",eliminar)
    else:
        for key in eliminar_turistas:
            print (f"Se elimino al turista: {turistas[key][0]}")
            del(turistas[key])
def turistas_por_mes(mes):
    total_turistas = len(turistas)
    visitantes_chile_en_mes = 0
    for datos in turistas.values():
        fecha = datos[2]
        mes_turista = int(fecha.split("-")[1])
        pais = datos[1].lower()

        if mes_turista == mes and pais == "chile":
            visitantes_chile_en_mes += 1
    
    porcentaje = (visitantes_chile_en_mes/ total_turistas) * 100
    return round(porcentaje,1)
def agregar_turista():
    while True:
        nuevo_id = input("Ingrese un ID con 3 digitos para el nuevo turista (Por ejemplo 016): ")
        if nuevo_id in turistas:
            print ("Ese ID ya existe.Ingrese uno diferente.")
        else:
            break

    nombre = input("Ingrese el nombre del turista: ")
    pais = input ("Ingrese el pais de origen: ")
    
    while True:
        fecha = input("Ingrese la fecha de visita (Formato dd-mm-aaaa): ")
        try:
            dia, mes, anio = map(int, fecha.split("-"))
            if 1 <= dia <= 31 and 1 <= mes <= 12 and anio >= 2000:
                break
            else:
                print("Fecha invalida. Intente de nuevo")
        except:
            print ("Formato incorrecto. Use dd-mm-aaaa")
    
    turistas[nuevo_id] = [nombre,pais,fecha]
    print(f"Turista {nombre} Agregado correctamente.")    
while True:
    print ("""
           ***MENU PRINCIPAL***
           1.Turista por pais
           2.Turistas por mes
           3.Eliminar turista
           4.Agregar turista
           6.Salir del menu          
           """)
    try:
        opcion = int(input("Eliga una opcion del menu (1-4): "))
    except ValueError:
        print ("Debes elegir una opcion del menu porfavor 1.2.3.4")
        continue
    if opcion == 6:
        print("Saliendo del menu...")
        break
    elif opcion == 1:
        pais = input("eliga el pais: ")
        turista_por_pais(pais)
    elif opcion == 2:
        try:
            mes = int(input("Eliga un mes (1/12): "))
        except ValueError as error:
            print(error)
            print("Debes elegir un mes valido donde 1 es enero y 12 es diciembre.")
            continue
        if mes >=1 and mes <=12:
            porcentaje = turistas_por_mes(mes)
            print(f"El numero de turistas que visitaron chile en el mes {mes} equivale al {porcentaje}")
    elif opcion == 3:
        eliminar = input("Ingrese el nombre a eliminar: ")
        turista_por_eliminar(eliminar)
    elif opcion == 4:
        agregar_turista()