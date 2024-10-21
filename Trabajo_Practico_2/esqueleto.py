import PIL
from PIL import ImageTk
import funciones_tp2
import numpy as np 
import tkinter as TK

links=('fotos/beach.jpg','fotos/bench.jpg','fotos/castle.jpg', 'fotos/dali.jpg', 
       'fotos/dali2.jpg', 'fotos/dolphin.jpg', 'fotos/lake.jpg', 'fotos/messi.webp')

def main():

    Imagen_RGB= input('Ingrese el link de la foto: ')
    if Imagen_RGB not in links:
        print('No se encontro la imagen...')
        return
    Matriz=funciones_tp2.imagen_a_matriz(Imagen_RGB)
    print(f'Las dimensiones originales son {Matriz.shape[0]} x {Matriz.shape[1]}')
    nuevo_ancho = int(input("Ingrese un nuevo ancho: "))
    nuevo_alto = int(input("Ingrese un nuevo largo: "))
    if nuevo_ancho < 0 or nuevo_alto < 0 or nuevo_ancho > Matriz.shape[1] or nuevo_alto > Matriz.shape[0]:
        print('El ancho o alto no pueden ser negativos ni mayor a su ancho o alto original')
        return

    Matrices=[]
    
    
    while Matriz.shape[1] > nuevo_ancho:

        hacer_padding= funciones_tp2.padding(Matriz)

        hacer_padding_r = hacer_padding[:,:,0]
        hacer_padding_g = hacer_padding[:,:,1]
        hacer_padding_b = hacer_padding[:,:,2] 

        sobel_x_r, sobel_y_r = funciones_tp2.aplicar_sobel(hacer_padding_r)
        sobel_x_g, sobel_y_g = funciones_tp2.aplicar_sobel(hacer_padding_g)
        sobel_x_b, sobel_y_b = funciones_tp2.aplicar_sobel(hacer_padding_b)

        sobel_x_promedio = (sobel_x_r + sobel_x_g + sobel_x_b) / 3
        sobel_y_promedio = (sobel_y_r + sobel_y_g + sobel_y_b) / 3

        gradiente=funciones_tp2.caclular_gradiente(sobel_x_promedio,sobel_y_promedio)

        matriz_energia_acumulada = funciones_tp2.matriz_energia_acumulada_columnas(gradiente)


        costura_columnas=funciones_tp2.costura_de_menor_energia_columnas(matriz_energia_acumulada)

        eliminar_columnas=funciones_tp2.eliminar_costuras_columnas(Matriz , costura_columnas)

        Matriz = eliminar_columnas
        Matrices.append(Matriz)


    while Matriz.shape[0] > nuevo_alto:

        hacer_padding= funciones_tp2.padding(Matriz)

        hacer_padding_r = hacer_padding[:,:,0]
        hacer_padding_g = hacer_padding[:,:,1]
        hacer_padding_b = hacer_padding[:,:,2] 

        sobel_x_r, sobel_y_r = funciones_tp2.aplicar_sobel(hacer_padding_r)
        sobel_x_g, sobel_y_g = funciones_tp2.aplicar_sobel(hacer_padding_g)
        sobel_x_b, sobel_y_b = funciones_tp2.aplicar_sobel(hacer_padding_b)

        sobel_x_promedio = (sobel_x_r + sobel_x_g + sobel_x_b) / 3
        sobel_y_promedio = (sobel_y_r + sobel_y_g + sobel_y_b) / 3

        gradiente=funciones_tp2.caclular_gradiente(sobel_x_promedio,sobel_y_promedio)

        matriz_energia_acumulada = funciones_tp2.matriz_energia_acumulada_filas(gradiente)

        costura_filas=funciones_tp2.costura_de_menor_energia_filas(matriz_energia_acumulada)

        eliminar_filas=funciones_tp2.eliminar_costuras_filas(Matriz, costura_filas)
        Matriz = eliminar_filas
        Matrices.append(Matriz)


    
    ventana= TK.Tk()
    imagen_visible=TK.Label(ventana,image=PIL.ImageTk.PhotoImage(PIL.Image.fromarray(Matrices[0])))
    imagen_visible.pack()
    slider = TK.Scale(ventana, from_=0, to=len(Matrices)-1, orient='horizontal', command=lambda texto_slider: funciones_tp2.callback(imagen_visible, PIL.ImageTk.PhotoImage(PIL.Image.fromarray(Matrices[int(texto_slider)]))))
    slider.pack()
    ventana.mainloop()


if __name__ == "__main__":
    main()

