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