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
    """ 
    Funcion que aplica filtros a un input ingresado y devuelve un output con los filtros aplicados
    PARAMETROS:
        matriz:np.ndarray
    RETORNA:
        (x)matriz(con filtros aplicados):np.ndarray
        (y)matriz(con filtros aplicados):np.ndarray
    """
    sobel_x = np.array([[1, 0, -1],
                        [2, 0, -2],
                        [1, 0, -1]]) 
    sobel_y = np.array([[1, 2, 1], 
                        [0, 0, 0],
                        [-1, -2, -1]])
    
    #llamo a la matriz con padding

    #dimensiones de la matriz y kernels para aplicar el filtro sobel
    alto,ancho = matriz.shape
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
            vecindad = matriz[i:i+ alto_kernel,a:a+ ancho_kernel]
            
            #hacer suma y multiplicacion de kernels para cada sobel
            matriz_salida_x[i,a] = np.sum(vecindad * sobel_x)
            matriz_salida_y[i,a] = np.sum(vecindad * sobel_y)
    
    return matriz_salida_x, matriz_salida_y 

def caclular_gradiente(sobel_x,sobel_y):

    
    gradiente = np.sqrt(sobel_x**2 + sobel_y**2)
    
    return gradiente

#quinta funcion crear matriz de energia
def matriz_energia(matriz:np.ndarray)->np.ndarray:
    """ 
    Funcion que crea la matriz de energia 
    PARAMETROS:
        matriz:np.ndarray
    RETORNA:
        matriz:np.ndarray

    """
    sobel_y,sobel_x = aplicar_sobel(matriz)
    energia = caclular_gradiente(sobel_x,sobel_y)
    
    return energia

def matriz_energia_acumulada_columnas(energia:np.ndarray)->np.ndarray:
    alto , ancho = energia.shape
    matriz_energia_columnas=np.zeros((alto , ancho ))
    energia_acumulada_columnas[0,:]=energia[0,:]
    
    for i in range (1, alto):
        for j in range (ancho):
            energia_acumulada[i,j]=energia[i,j] + min(
                energia_acumulada_columnas[i-1, j], 
                energia_acumulada_columnas[i-1 , j-1] if j >0 else np.inf,
                energia_acumulada_columnas[i-1 , j+1] if j < ancho - 1 else np.inf
            )
    return energia_acumulada


def costura_de_menor_energia_columnas (energia_acumulada:np.ndarray)-> np.ndarray:
    """ 
    Funcion que selecciona un pixel x cada fila para formar una columna 
    PARAMETROS:
        energia acumulada: matriz de energia acumulada
    RETORNA:
        costura_columnas: matriz con una columna formada por pixeles en cada fila 
    """
    alto , ancho =energia_acumulada.shape
    costura=np.zeros(alto)
    ultima_fila=energia_acumulada[:-1]
    valor_minimo=np.argmin(ultima_fila)
    costura[-1]=valor_minimo
    penultima_fila=ultima_fila -1
    for i in range (alto-2 , -1 , -1):
        j=costura[i+1]
        costura[i]= j + np.argmin([
            energia_acumulada[i , j],
            energia_acumulada[i , j-1] if j > 0 else np.inf , 
            energia_acumulada[i , j+1] if j < 0 else np.inf
        ])-1
    return costura_columnas

def costura_de_menor_energia_filas (energia_acumulada:np.ndarray) -> np.ndarray:
    """ 
    Funcion que agarra un pixel por cada columna para generar una fila  
    PARAMETROS:
        energia acumulada: matriz de energia acumulada
    RETORNA:
        costura_filas: matriz con una fila por pixeles 
    """
    alto , ancho =energia_acumulada.shape
    costura=np.zeros(alto)
    ultima_columna=energia_acumulada[:,-1]
    valor_minimo=np.argmin(ultima_fila)
    costura[:,-1]=valor_minimo
    penultima_fila=ultima_columna -1
    for j in range (ancho-2 , -1 , -1):
        i=costura[j+1]
        costura[j]= i + np.argmin([
            energia_acumulada[i , j],
            energia_acumulada[i-1 , j] if i > 0 else np.inf , 
            energia_acumulada[i+1 , j] if i < 0 else np.inf
        ])-1
    return costura_filas

def eliminar_costuras_filas (matriz_rgb , costura_columnas ):
    """
    Funcion que elimina las filas seleccionadas en la funcion anterior 
    PARAMETROS:
        matriz_rgb
        costura_columnas
    RETORNA:
        nueva matriz: con una columna menos 
    """
    alto , ancho , canales= matriz_rgb.shape
    nueva_matriz=np.zeros(alto, ancho - len(costura_columnas) , canales)
    j=costura_columnas[i]
    nueva_matriz[i]=np.delete(matriz_rgb , j , axis=0) #axis=0 filas #axis=1 columnas #axis=2 canales
    return nueva_matriz


def eliminar_costuras_columnas ( matriz_rgb , costura_filas):
    """
    Funcion que elimina las filas seleccionadas en la funcion anterior 
    PARAMETROS:
        matriz_rgb
        costura_filas
    RETORNA:
        nueva matriz:con una fila menos
    """
    alto , ancho , canales= matriz_rgb.shape
    nueva_matriz=np.zeros(alto-len(costura_filas), ancho, canales)
    i=costura_filas[j]
    nueva_matriz[j]=np.delete(matriz_rgb , i , axis=1) #axis=0=filas #axis=1=columnas #axis=2=canales
    return nueva_matriz

def mostrar_imagen_final (imagen):
    imagen = (imagen - imagen.min()) /(imagen.max() - imagen.min()) * 255
    imagen = imagen.astype(np.uint8)
    imagen_final=Image.fromarray(imagen)
    imagen_final.show(title="Imagen final de la matriz original")

