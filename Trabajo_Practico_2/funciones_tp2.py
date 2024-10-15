import numpy as np 

from PIL import Image

def imagen_a_matriz(foto:str)->int:
    """

    Funcion que transforma imagenes en mateices:

    Parametros:
        foto:str
        matriz:int

    Retorna:
    """ 

    imagen=Image.open(foto)
    print(imagen)

    matriz=np.array(imagen)
    print(matriz)
    return matriz




def generador_matrices_filter (matriz:int)-> int:
    """ 

    Funcion que se encarga de generar matrices filtros

    Parametros:
        matriz:int

    Reetorna:
    """ 

    (type(matriz))
    print(matriz)

def padding (Matriz_rgb):
    alto,ancho,canales = Matriz_rgb.shape #shape nos da 3 valores y nosotros asignamos esos valores a largo ancho y canales
    matriz_padding= np.zeros((alto + 2 , ancho + 2 , canales ),dtype=Matriz_rgb.dtype) # crea una  matriz de ceros con 2 filas y columnas mas que la oiginal 
    matriz_padding[1:alto + 1, 1:ancho + 1, :] = Matriz_rgb #copiamos la matriz original en el centro de la matriz de ceros
    print('Matriz con padding')
    return matriz_padding

#def filtro_sobel (ancho, altura):


    

    

