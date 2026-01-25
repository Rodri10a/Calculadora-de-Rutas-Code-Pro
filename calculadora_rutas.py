import random
from collections import deque
import copy

class Mapa:
    def __init__(self, dim): 
        # MÉTODO CONSTRUCTOR: Sirve para inicializar el objeto.
        self.dim = dim
        self.tablero = [["⬜" for _ in range(self.dim)] for _ in range(self.dim)]
        self.jugador_pos = None 
        self.meta_pos = None

    def colocar_puntos(self, jugador_pos, meta_pos):
        # El Mapa es responsable de saber dónde están el jugador y la meta.
        self.jugador_pos = jugador_pos
        self.meta_pos = meta_pos
        self.tablero[jugador_pos[0]][jugador_pos[1]] = "🕵️‍♂️"
        self.tablero[meta_pos[0]][meta_pos[1]] = "🏁"

    def obstaculos(self, cantidad):
        for _ in range(cantidad):
            x = random.randint(0, self.dim - 1) 
            y = random.randint(0, self.dim - 1) 
            if self.tablero[x][y] == "⬜" and (x, y) not in (self.jugador_pos, self.meta_pos):
                self.tablero[x][y] = "💣" # se usa el self para llamar internamente 

    def agregar_obstaculo(self, x, y):
        self.tablero[x][y] = "❌" # agrego un objeto nuevo a mi tablero y por eso le paso self.tablero 

    def imprimir(self, tablero_a_mostrar=None):# el none sirve para que la funcion sea flexible y pueda usarse de dos maneras distintas 
        objetivo = tablero_a_mostrar or self.tablero
        # tablero_a_mostrar = None , pero self.tablero es el mapa original de la clase ''
        for fila in objetivo: 
            print("".join(fila))

class BuscadorRutas:
    def __init__(self, mapa): 
        self.mapa = mapa # permite una mejor separacion de responsabilidades 

    def bfs(self):
        inicio = self.mapa.jugador_pos # es como decir que use un puntero para que use los datos que ya tenemos 
        meta = self.mapa.meta_pos
        dim = self.mapa.dim  
        
        movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visitado = [[False for _ in range(dim)] for _ in range(dim)]
        padre = {}
        cola = deque([inicio])
        
        visitado[inicio[0]][inicio[1]] = True
        padre[inicio] = None
        
        while cola:
            actual = cola.popleft() # saca la casilla mas antigua para analizar sus vecinos 
            if actual == meta:
                break
            
            x, y = actual
            for dx, dy in movimientos:
                nx, ny = x + dx, y + dy
                if 0 <= nx < dim and 0 <= ny < dim:
                    if not visitado[nx][ny] and self.mapa.tablero[nx][ny] not in ["💣", "❌"]: 
                        visitado[nx][ny] = True # vecino visitado, se mete a la cola 
                        padre[(nx, ny)] = actual # es para saber de donde vine 
                        cola.append((nx, ny)) 
        
        if meta not in padre:
            return None
            
        ruta = []
        actual = meta
        while actual is not None:
            ruta.append(actual)
            actual = padre[actual]
        ruta.reverse()
        return ruta

# --- LÓGICA DE INTERFAZ (EL BUCLE PRINCIPAL) ---

print("CALCULADORA DE RUTAS USANDO BFS")

while True:
    try:
        dim = int(input("\nUna recomendacion para que el mapa se vea mejor de 8-15 en adelante 😎\nIngrese el tamaño del mapa: "))
        if dim < 6:
            print("❌El mapa debe ser al menos de 6x6")
            continue
        break
    except ValueError:
        print("❌Ingresaste un tamaño de tablero invalido\nIngresa un nuevo tamaño por favor")

# Instanciamos el mapa
mi_mapa = Mapa(dim) # esto seria el corazon de mi programa CONTENEDOR GLOBAL

while True:
    try:
        jugador_x = int(input("Ingresa la coordenada x del jugador\n"))
        jugador_y = int(input("Ingresa la coordenada y del jugador\n"))
        if not (0 <= jugador_x < dim and 0 <= jugador_y < dim):
            print("Coordenadas fuera de rango\nIngrese una coordenada valida")
            continue
        
        meta_x = int(input("Ingresa la coordenada x para la meta\n"))
        meta_y = int(input("Ingresa la coordenada y para la meta\n"))
        if not (0 <= meta_x < dim and 0 <= meta_y < dim):
            print("Coordenadas fuera de rango\nIngrese una coordenada valida")
            continue
        
        if (jugador_x, jugador_y) == (meta_x, meta_y):
            print("El jugador y la meta no pueden estar en la misma posicion")
            continue
        break
    except ValueError:
        print("Ingrese coordenadas validas ")

mi_mapa.colocar_puntos((jugador_x, jugador_y), (meta_x, meta_y))

cant_obstaculos = int(input("\nUna recomendacion para que sea mejor la experiencia es que no haya mas de 15 obstaculos\nIngrese la cantidad de obstaculos en el tablero: "))
mi_mapa.obstaculos(cant_obstaculos)

print("TABLERO INICIAL")
mi_mapa.imprimir()

# Instanciamos la calculadora pasándole el mapa
calculadora = BuscadorRutas(mi_mapa) # para que sepa el valor actualizado 

def procesar_ruta(ruta_encontrada):
    if ruta_encontrada:
        print("Ruta encontrada !!")
        tablero_solucion = copy.deepcopy(mi_mapa.tablero) # hace un copia sin dañar al tablero original 
        for (rx, ry) in ruta_encontrada:
            if (rx, ry) != mi_mapa.jugador_pos and (rx, ry) != mi_mapa.meta_pos:
                tablero_solucion[rx][ry] = "🟢"
        mi_mapa.imprimir(tablero_solucion)
        
        print("Pasos de la ruta en coordenadas")
        for i, (x, y) in enumerate(ruta_encontrada):
            if i == 0 :
                print (f" Inicio: ({x}, {y})") 
            else: 
                print (f" Pasos {i}: ({x}, {y})") 
        return True 
    else:
        print("No existe camino posible hasta la meta 😢😢")
        return False

print("TABLERO RESUELTO CON BFS")
if not procesar_ruta(calculadora.bfs()): 
    exit() 

while True:
    respuesta = input("Desea agregar un nuevo obstaculo ? (si/no): ").lower()
    if respuesta == "no":
        print("Laberinto finalizado. Gracias por jugar !!")
        break
    elif respuesta == "si":
        while True:
            try:
                nuevo_x = int(input("Ingresa la coordenada x del nuevo obstaculo: "))
                nuevo_y = int(input("Ingresa la coordenada y del nuevo obstaculo: "))
                if not (0 <= nuevo_x < dim and 0 <= nuevo_y < dim):
                    print("Coordenadas fuera de rango. Intente de nuevo. ")
                    continue
                if (nuevo_x, nuevo_y) in [mi_mapa.jugador_pos, mi_mapa.meta_pos]: 
                    # si crea una lista de dos tuplas con su valor de x y y, si esta en alguno de ellos no se puede poner el obstaculo 
                    print("No podes poner el obstaculo donde esta el jugador o la meta")
                    continue
                mi_mapa.agregar_obstaculo(nuevo_x, nuevo_y)
                break
            except ValueError:
                print("Ingrese coordenadas validas ")
        
        nueva_ruta = calculadora.bfs() 
        if nueva_ruta:
            print("TABLERO RESUELTO CON EL NUEVO OBSTACULO")
            procesar_ruta(nueva_ruta)
        else:
            mi_mapa.imprimir()
            print("No existe ninguna ruta posible hacia la meta 😥")
            break
    else:
        print("Ingresa una opcion valida (si o no)")