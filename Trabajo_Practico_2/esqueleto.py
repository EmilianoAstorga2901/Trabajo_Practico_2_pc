import funciones_tp2
import numpy as np
import PIL
foto1='fotos/castle.jpg'
Imagen_RGB=foto1
Matriz=funciones_tp2.imagen_a_matriz(Imagen_RGB)
hacer_padding= funciones_tp2.padding(Matriz)
print(hacer_padding)
print(Matriz.shape)
print(hacer_padding.shape)
hacer_padding_r = hacer_padding[:,:,0]
hacer_padding_g = hacer_padding[:,:,1]
hacer_padding_b = hacer_padding[:,:,2] 
sobel_x_r, sobel_y_r = funciones_tp2.aplicar_sobel(hacer_padding_r)
sobel_x_g, sobel_y_g = funciones_tp2.aplicar_sobel(hacer_padding_g)
sobel_x_b, sobel_y_b = funciones_tp2.aplicar_sobel(hacer_padding_b)
sobel_x_promedio = (sobel_x_r + sobel_x_g + sobel_x_b) / 3
sobel_y_promedio = (sobel_y_r + sobel_y_g + sobel_y_b) / 3
gradiente=funciones_tp2.caclular_gradiente(sobel_x_promedio,sobel_y_promedio)
matriz_energia=funciones_tp2.matriz_energia(gradiente)
Imagen_matriz_energia=funciones_tp2.mostrar_imagen_final(matriz_energia)

