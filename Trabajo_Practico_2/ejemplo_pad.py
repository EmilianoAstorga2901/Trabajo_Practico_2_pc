import numpy as np
import PIL
import funciones_tp2
foto1='fotos/beach.jpg'
Matriz_rgb=funciones_tp2.imagen_a_matriz(foto1)
alto,ancho,canales = Matriz_rgb.shape #shape nos da 3 valores y nosotros asignamos esos valores a largo ancho y canales
matriz_padding= np.zeros((alto + 2 , ancho + 2 , canales ),dtype=Matriz_rgb.dtype) # crea una  matriz de ceros con 2 filas y columnas mas que la oiginal 
matriz_padding[1:alto + 1, 1:ancho + 1, :] = Matriz_rgb #copiamos la matriz original en el centro de la matriz de ceros
print('Matriz con padding')
print(matriz_padding)

