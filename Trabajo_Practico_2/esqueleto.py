import funciones_tp2
import numpy as np
foto1='fotos/beach.jpg'
foto2='fotos/bench.jpg'
foto3='fotos/castle.jpg'
foto4='fotos/dali.jpg'          #falta 1 foto
foto5='fotos/dali2.jpg'
foto6='fotos/dolphin.jpg'
foto7='fotos/lake.jpg'
Matriz=funciones_tp2.imagen_a_matriz(foto2)

filter=funciones_tp2.generador_matrices_filter(np.array([[1,2,0], [0,0,2],[0,2,2]]))
