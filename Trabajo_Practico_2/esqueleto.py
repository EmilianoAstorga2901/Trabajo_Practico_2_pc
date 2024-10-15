import funciones_tp2
import numpy as np
foto1='fotos/beach.jpg'
Matriz=funciones_tp2.imagen_a_matriz(foto1)

matriz_padding= funciones_tp2.padding(Matriz)
print(matriz_padding)

print("Filtros kernel")
Kernel_x=funciones_tp2.generador_matrices_filter(np.array([[-1,0,1], [-2,0,2],[-1,0,1]]))
Kernel_y=funciones_tp2.generador_matrices_filter(np.array([[-1,-2,-1],[0,0,0],[1,2,1]]))

