#
#Archivo: Mision Orbita final.py
#curso: SOFT-01 PRINCIPIOS DE PROGRAMACION 1 - Sección SCV6
#Estudiante: Dennis Alonso Lopez Quesada
#Fecha: 18/11/2026
#Version:1.0
#Descripcion: Este programa simula una mision espacial de un viaje de ida y vuelta, contando recursos y haciendo predicciones.







#Datos fijos
DESTINOS = (("luna", 3), ("Marte", 5), ("Europa", 7))



ACTIVIDADES = (
("Analizar terreno ", 0, 8, 0, 10),
("Recoletar muestra", 0, 12, 2, 20),
("Realizar observacion", 0 , 5, 0, 8),
("sobrevolaar la zona", 15, 3, 0, 25)
)




RECURSOS = ("combustible", "oxigeno", "energia","provisiones")
RECURSO_VITALES = ("oxigeno","energia","provisiones")
RESULTADOS = ("El regreso fue un exito", "El regreso fue interrumpido","La tripulacion esta varada","No hay autorizacion","No se planifico el viaje")






#Posicion de los recursos
COMBUSTIBLE = 0
OXIGENO = 1 
ENERGIA = 2
PROVISIONES = 3








#recordar el orden en las sangrias
    #Funciones 
def leer_recursos():
    print("\n--- INGRESO DE RECURSOS ---")
    valores_ingresados = []

    for nombre in RECURSOS:
        cantidad = int(input(f"Igrese la cantidad de {nombre} disponible: "))
        valores_ingresados.append(cantidad)

    # El return va fuera del for
    return valores_ingresados

def seleccionar_destino():
    print("\n--- SELECCION DE DESTINO ---")

    for i in range(len(DESTINOS)):
        nombre_planeta = DESTINOS[i][0]
        print(f"{i + 1}. {nombre_planeta}")

    opcion = int(input("Ingrese el numero del destino:"))
    destino_elegido = DESTINOS[opcion - 1]

    return destino_elegido

def elegir_actividad():
    print("\n--- SELECCION DE ACTIVIDAD ---")

    for i in range(len(ACTIVIDADES)):
        nombre_actividad = ACTIVIDADES[i][0]
        print(f"{i + 1}. {nombre_actividad}")

    opcion = int(input("Ingrese el numero de la actividad:"))
    actividad_elegida = ACTIVIDADES[opcion - 1]

    return actividad_elegida

# Programa principal pegado al margen izquierdo
if __name__ == "__main__":
    recursos_actuales = leer_recursos()
    print(f"Recursos iniciales: {recursos_actuales}")
   
    destino_actual = seleccionar_destino()
    print(f"Destino seleccionado: {destino_actual[0]} con factor de distancia: {destino_actual[1]}") 
    
    actividad_actual = elegir_actividad()
    print(f"Actividad seleccionada: {actividad_actual[0]}")

def calcular_requeridos(dias_viaje, tripulantes):
    req_combustible = dias_viaje * 8 * 2 + 10
    req_oxigeno = dias_viaje * 2 * 2 * tripulantes + 5
    req_energia = dias_viaje * 5 * 2 + 10
    req_provisiones = dias_viaje * tripulantes * 2 + 3

    return [req_combustible, req_oxigeno, req_energia, req_provisiones] 
