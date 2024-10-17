import tkinter as TK
from tkinter import ttk
from tkinter import simpledialog
from PIL import Image, ImageTk  
import os 

# Ventana principal
ventana = TK.Tk()
ventana.geometry('500x500')
ventana.resizable(False, False)
ventana.title('Slider Demo')

ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=3)

path_imagen = simpledialog.askstring("Ingrese la dirección de la imagen",
                                       "Ingrese la dirección de la imagen")
ancho_imagen = simpledialog.askinteger("Ingrese ancho de la imagen",
                                        "Ingrese ancho de la imagen")
alto_imagen = simpledialog.askinteger("Ingrese alto de la imagen",
                                       "Ingrese alto de la imagen")


if path_imagen is None or ancho_imagen is None or alto_imagen is None:
    print("No se cargaron los datos correctos")
    exit()

try:
    
    imagen_canvas = Image.open(path_imagen)
    imagen_canvas = imagen_canvas.resize((ancho_imagen, alto_imagen))
    
    
    imagen_canvas_resized_path = os.path.splitext(path_imagen)[0] + '_resized.jpg'
    imagen_canvas.save(imagen_canvas_resized_path, format='JPEG')

    
    image = ImageTk.PhotoImage(imagen_canvas)  
except FileNotFoundError:
    print(f"Error: No se encontró el archivo en la ruta: {path_imagen}")
    exit()
except Exception as e:
    print(f"Error al cargar la imagen: {e}")
    exit()


canvas = TK.Canvas(ventana, height=400, width=400, bg='grey')
canvas.create_image(200, 200, image=image, anchor='center')  


current_value = TK.DoubleVar()

def get_current_value():
    return '{:.2f}'.format(current_value.get())

def slider_changed(event):
    value_label.configure(text=get_current_value())


slider_label = ttk.Label(ventana, text='Slider:')
slider_label.grid(column=0, row=0, sticky='w')

slider = ttk.Scale(
    ventana,
    from_=0,  
    to=100,
    orient='horizontal',
    command=slider_changed,
    variable=current_value)

value_label = ttk.Label(ventana, text=get_current_value())
slider.grid(column=1, row=1, sticky='S')
canvas.grid(column=1, row=0, sticky='N')
value_label.grid(row=2, columnspan=2, sticky='n')

ventana.mainloop()

