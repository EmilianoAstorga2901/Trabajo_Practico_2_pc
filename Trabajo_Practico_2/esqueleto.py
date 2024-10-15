import funciones_tp2
import numpy as np
foto1='fotos/beach.jpg'
Matriz=funciones_tp2.imagen_a_matriz(foto1)

matriz_padding= funciones_tp2.padding(Matriz)
print(matriz_padding)
print(Matriz.shape)
print(matriz_padding.shape)

matriz_horizontal, matriz_vertical = funciones_tp2.aplicar_sobel(matriz_padding)
print('matriz_horizontal')
print(matriz_horizontal)
print('matriz vertical')
print(matriz_vertical)


