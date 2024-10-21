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

    matriz=np.array(imagen)
    
    return matriz


def padding (Matriz_rgb:np.ndarray)->np.ndarray:
    """ 
    Funcion que crea una matriz de ceros y pega la matriz de imagen adentro de la de ceros 
    Parametros:
        Matriz_rgb:Matriz de una imagen con 3 canales rojo verde y azul 
    Retorna:
        matriz_padding:Matriz rodeada de ceros
    """
    
    alto,ancho,canales = Matriz_rgb.shape
    matriz_padding= np.zeros((alto + 2 , ancho + 2 , canales ),dtype=Matriz_rgb.dtype) 
    matriz_padding[1:alto + 1, 1:ancho + 1, :] = Matriz_rgb 
    
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
    

    
    alto,ancho = matriz.shape
    alto_kernel , ancho_kernel = sobel_x.shape
    
    salida_alto = alto - alto_kernel +1
    salida_ancho = ancho - ancho_kernel +1
    
    
    matriz_salida_x = np.zeros((salida_alto,salida_ancho))
    matriz_salida_y = np.zeros((salida_alto,salida_ancho))
    
    
    for i in range(salida_alto):
        for a in range(salida_ancho):
            
            vecindad = matriz[i:i+ alto_kernel,a:a+ ancho_kernel]
            
            matriz_salida_x[i,a] = np.sum(vecindad * sobel_x)
            matriz_salida_y[i,a] = np.sum(vecindad * sobel_y)
    
    return matriz_salida_x, matriz_salida_y 

def caclular_gradiente(sobel_x,sobel_y):

    
    gradiente = np.sqrt(sobel_x**2 + sobel_y**2)
    
    return gradiente


def matriz_energia_acumulada_columnas(energia:np.ndarray)->np.ndarray:
    
    alto , ancho = energia.shape
    energia_acumulada=np.zeros((alto , ancho ))
    energia_acumulada[0,:]=energia[0,:]
    
    for i in range (1, alto):
        for j in range (ancho):
            energia_acumulada[i,j]=energia[i,j] + min(
                energia_acumulada[i-1, j], 
                energia_acumulada[i-1 , j-1] if j >0 else np.inf,
                energia_acumulada[i-1 , j+1] if j < ancho - 1 else np.inf
            )
    
    return energia_acumulada


def matriz_energia_acumulada_filas(energia:np.ndarray)->np.ndarray:
    
    alto , ancho = energia.shape
    energia_acumulada=np.zeros((alto , ancho ))
    energia_acumulada[0,:]=energia[0,:]
    
    for j in range (1, ancho):
        for i in range (alto):
            energia_acumulada[i,j]=energia[i,j] + min(
                energia_acumulada[i, j-1], 
                energia_acumulada[i-1 , j-1] if i >0 else np.inf,
                energia_acumulada[i+1 , j-1] if i < alto - 1 else np.inf
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
    costura_columnas=np.zeros(alto , dtype=int)

    ultima_fila=energia_acumulada[-1]
    valor_minimo=np.argmin(ultima_fila)
    costura_columnas[-1]=valor_minimo
    
    for i in range (alto-2 , -1 , -1):
        j=costura_columnas[i+1]
        
        izquierda = energia_acumulada[i, j - 1] if j > 0 else np.inf
        centro = energia_acumulada[i , j]
        derecha = energia_acumulada[i, j + 1] if j < ancho - 1 else np.inf

        costura_columnas[i] = j +  np.argmin([izquierda,centro,derecha]) - 1
    
    return costura_columnas

def costura_de_menor_energia_filas (energia_acumulada:np.ndarray) -> np.ndarray:
    """ 
    Funcion que agarra un pixel por cada columna para generar una fila  
    PARAMETROS:
        energia acumulada: matriz de energia acumulada
    RETORNA:
        costura_filas: matriz con una fila por pixeles 
    """
    alto , ancho = energia_acumulada.shape
    costura_filas = np.zeros(ancho, dtype=int)

    ultima_columna = energia_acumulada[:,-1]
    valor_minimo = np.argmin(ultima_columna)
    costura_filas[-1] = valor_minimo

    for j in range (ancho-2 , -1 , -1):
        i = costura_filas[j+1]
        
        arriba = energia_acumulada[i - 1, j] if i > 0 else np.inf
        centro = energia_acumulada[i,j]
        abajo =  energia_acumulada[i + 1, j] if i < alto - 1 else np.inf

        costura_filas[j] = i + np.argmin([arriba,centro,abajo]) - 1

    return costura_filas

def eliminar_costuras_filas (matriz_rgb:np.ndarray , costura_columnas:np.ndarray ) -> np.ndarray:
    """
    Funcion que elimina las filas seleccionadas en la funcion anterior 
    PARAMETROS:
        matriz_rgb
        costura_columnas
    RETORNA:
        nueva matriz: con una columna menos 
    """
    alto , ancho , canales= matriz_rgb.shape
    nueva_matriz=np.zeros((alto-1, ancho , canales), dtype = np.uint8)
    
    for j in range(len(costura_columnas)):
        y=costura_columnas[j]
        nueva_matriz[:,j,:]=np.delete(matriz_rgb[:,j,:] , y , axis=0)

    return nueva_matriz


def eliminar_costuras_columnas ( matriz_rgb:np.ndarray , costura_filas:np.ndarray)-> np.ndarray:
    """
    Funcion que elimina las filas seleccionadas en la funcion anterior 
    PARAMETROS:
        matriz_rgb
        costura_filas
    RETORNA:
        nueva matriz:con una fila menos
    """
    alto , ancho , canales= matriz_rgb.shape
    nueva_matriz=np.zeros((alto, ancho-1, canales), dtype=np.uint8)
    
    for i in range(len(costura_filas)):
        x=costura_filas[i]
        nueva_matriz[i]=np.delete(matriz_rgb[i] , x , axis=0) 
    
    return nueva_matriz

def mostrar_imagen_final(imagen):
    if imagen.size == 0:
        return'La imagen esta vacia'
    imagen = (imagen - imagen.min()) / (imagen.max() - imagen.min()) * 255
    imagen_ = imagen.astype(np.uint8)
    
    imagen_final = Image.fromarray(imagen_)
    imagen_final.show()


def callback(imagen_visible,imagen):
    imagen_visible.config(image=imagen)
    imagen_visible.image=imagen