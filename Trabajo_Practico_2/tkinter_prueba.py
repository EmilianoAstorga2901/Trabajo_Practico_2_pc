import tkinter as tk
from tkinter import ttk
import tkinter
from tkinter import simpledialog
from PIL import Image

# root window
ventana = tk.Tk()
ventana.geometry('500x500')
ventana.resizable(False, False)
ventana.title('Slider Demo')

ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=3)

path_imagen = simpledialog.askstring("ingrese la direccion de la imagen",
                                     "ingrese la direccion de la imagen")
ancho_imagen = simpledialog.askinteger("ingrese ancho de la imagen",
                                       "ingrese ancho de la imagen")
alto_imagen = simpledialog.askinteger("ingrese alto de la imagen",
                                      "ingrese alto de la imagen")

if path_imagen is None or ancho_imagen is None or alto_imagen is None:
  print("No se cargaron los datos correctos")
  exit()

try:
    imagen_canvas = Image.open(path_imagen)
    imagen_canvas = imagen_canvas.resize((ancho_imagen, alto_imagen))
    imagen_canvas_resized_path = os.path.splitext(path_imagen)[0] + '_resized.jpg'
    imagen_canvas.save(imagen_canvas_resized_path, format='JPEG')

    image = ImageTk.PhotoImage(imagen_canvas)
except Exception as e:
    print(f"Error al cargar la imagen: {e}")
    exit()
canvas = tk.Canvas(ventana, height=400, width=400, bg='red')
canvas.create_image(400, 400, image=image, anchor='se')
# slider current value
current_value = tk.DoubleVar()


def get_current_value():
  return '{: .2f}'.format(current_value.get())


def slider_changed(event):
  value_label.configure(text=get_current_value())


# label for the slider
slider_label = ttk.Label(ventana, text='Slider:')

slider_label.grid(column=0, row=0, sticky='w')

#  slider
slider = ttk.Scale(
    ventana,
    from_=0,  # rango o valores que puede tomar el slicer [0, 100]
    to=100,
    orient='horizontal',  # vertical
    command=slider_changed,  # evento que maneja el slider
    variable=current_value)

# current value label

value_label = ttk.Label(ventana, text=get_current_value())
slider.grid(column=1, row=1, sticky='S')
canvas.grid(column=1, row=0, sticky='N')
value_label.grid(row=2, columnspan=2, sticky='n')

ventana.mainloop()

