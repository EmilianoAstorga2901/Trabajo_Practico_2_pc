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
    """ 
    Funcion que crea una matriz de ceros y pega la matriz de imagen adentro de la de ceros 
    Parametros:
        Matriz_rgb:Matriz de una imagen con 3 canales rojo verde y azul 
    Retorna:
        matriz_padding:Matriz rodeada de ceros
    """
    alto,ancho,canales = Matriz_rgb.shape #shape nos da 3 valores y nosotros asignamos esos valores a largo ancho y canales
    matriz_padding= np.zeros((alto + 2 , ancho + 2 , canales ),dtype=Matriz_rgb.dtype) # crea una  matriz de ceros con 2 filas y columnas mas que la oiginal 
    matriz_padding[1:alto + 1, 1:ancho + 1, :] = Matriz_rgb #copiamos la matriz original en el centro de la matriz de ceros
    print('Matriz con padding')
    return matriz_padding

def aplicar_sobel(matriz: np.ndarray) -> np.ndarray:
    sobel_x = np.array([[1, 0, -1],
                        [2, 0, -2],
                        [1, 0, -1]]) 
    sobel_y = np.array([[1, 2, 1], 
                        [0, 0, 0],
                        [-1, -2, -1]])
    
    #llamo a la matriz con padding
    matriz_padding = padding(matriz)

    #dimensiones de la matriz y kernels para aplicar el filtro sobel
    alto,ancho,canales = matriz_padding.shape
    alto_kernel , ancho_kernel = sobel_x.shape
    
    salida_alto = alto - alto_kernel
    salida_ancho = ancho - ancho_kernel
    
    #matriz para guardar los resultados
    matriz_salida_x = np.zeros((salida_alto,salida_ancho))
    matriz_salida_y = np.zeros((salida_alto,salida_ancho))
    
    #convolucion para sobel x e y
    for i in range(salida_alto):
        for a in range(salida_ancho):
            
            #vecindad de cada pixel
            vecindad = matriz_padding[i:i+ alto_kernel,a:a+ ancho_kernel]
            
            #hacer suma y multiplicacion de kernels para cada sobel
            matriz_salida_x[i,a] = np.sum(vecindad * sobel_x)
            matriz_salida_y[i,a] = np.sum(vecindad * sobel_y)
    
    return matriz_salida_y, matriz_salida_x 

def caclular_gradiente(sobel_x,sobel_y):
    
    gradiente = np.sqrt(sobel_x*2 + sobel_y*2)
    
    return gradiente

#quinta funcion crear matriz de energia
def matriz_energia(matriz):
    
    sobel_y,sobel_x = aplicar_sobel(matriz)
    energia = caclular_gradiente(sobel_x,sobel_y)
    
    return energia

def matriz_energia_acumulada (energia):
    alto , ancho = energia.shape
    energia_acumulada=np.zeros(alto , ancho )
    energia_acumulada[0,:]=energia[0,:]
    
    for i in range (1, alto):
        for j in range (ancho):
            energia_acumulada[i,j]=energia[i,j] + min(
                energia_acumulada[i-1, j], 
                energia_acumulada[i-1 , j-1] if j >0 else np.inf,
                energia_acumulada[i-1 , j+1] if j < ancho - 1 else np.inf
            )
    return energia_acumulada            

    

    

