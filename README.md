# 🗺️ Calculadora de Rutas — BFS Pathfinder

Calculadora interactiva de rutas que utiliza el algoritmo BFS (Breadth-First Search) para encontrar el camino más corto entre dos puntos en un mapa con obstáculos. Desarrollado en Python puro, sin dependencias externas.

## 📋 Descripción

El programa genera un tablero de dimensiones personalizables donde el usuario coloca un punto de inicio 🕵️‍♂️ y una meta 🍎. Se pueden agregar obstáculos aleatorios 💣 o manuales ❌, y el algoritmo BFS calcula la ruta más corta evitando dichos obstáculos. La ruta se visualiza directamente en la terminal con emojis.
Características principales

## Mapa dinámico: dimensiones configurables (mínimo 6×6).

Obstáculos aleatorios y manuales: se pueden combinar ambos tipos.
Visualización con emojis: el tablero se imprime en consola de forma clara y visual.
Recalculación en tiempo real: tras agregar un nuevo obstáculo, el algoritmo recalcula la ruta automáticamente.
Diseño orientado a objetos: separación de responsabilidades entre el mapa (Mapa) y el buscador de rutas (BuscadorRutas).


## Cómo ejecutar

Requisitos

## Python 3.8 o superior.

Una terminal con soporte para emojis (la mayoría de terminales modernas lo soportan).

## Ejecución

bashpython calculadora_rutas.py


## 🎮 Flujo de uso

- Definir el tamaño del mapa — se recomienda entre 8 y 15 para una mejor visualización.
- Colocar al jugador — ingresar coordenadas (x, y) del punto de inicio.
- Colocar la meta — ingresar coordenadas (x, y) del punto de destino.
- Agregar obstáculos aleatorios — definir la cantidad (se recomienda no más de 15).
- Ver la ruta calculada — el programa muestra el camino más corto con 🟢.
- Agregar obstáculos manualmente (opcional) — se puede seguir agregando obstáculos y el algoritmo recalcula la ruta.

