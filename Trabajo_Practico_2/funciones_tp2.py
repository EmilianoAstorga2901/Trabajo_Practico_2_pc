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



def generador_matrices_filter (matriz:int)-> int:
    """ 

    Funcion que se encarga de generar matrices filtros

    Parametros:
        matriz:int

    Reetorna:
    """ 

    print(type(matriz))
    print(matriz)

#def padding (matriz):
#   padding = np.pad(matriz, ((1,1), (1,1)),constant_values=0)
 #   return padding

    









#def convolucion (input:int , filter: int) ->int :
    

