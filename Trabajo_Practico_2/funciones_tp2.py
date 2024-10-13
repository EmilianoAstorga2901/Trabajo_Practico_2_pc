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
    Funcion que se encarga de generar matrices 
    Parametros:
        matriz:int
    Reetorna:
    """ 
    print(type(matriz))
    print(matriz)

def padding (matriz:int,filter:int):
    
    filter=np.array(x,y,z)
    print(filter)
    matriz_padding=str(matriz) 
    








#def convolucion (input:int , filter: int) ->int :
    
