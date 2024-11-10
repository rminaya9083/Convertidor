# screen.py

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from convertir_a_cpp import convertir_a_cpp

# Función para manejar la conversión
def convertir():
    codigo_python = text_input.get("1.0", "end-1c")  # Obtener el texto de la caja de entrada
    if not codigo_python.strip():  # Verificar si el código está vacío
        messagebox.showwarning("Advertencia", "Por favor ingresa un código Python.")
        return
    
    try:
        codigo_cpp = convertir_a_cpp(codigo_python)
        text_output.config(state="normal")  # Habilitar la caja de texto de salida
        text_output.delete("1.0", "end")  # Limpiar el contenido previo
        text_output.insert("1.0", codigo_cpp)  # Insertar el código C++ convertido
        text_output.config(state="disabled")  # Deshabilitar la edición
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al convertir el código: {e}")

# Crear la ventana principal
root = ttk.Window(themename="darkly")  # Cambia el tema aquí (ej: flatly, darkly, cyborg, etc.)
root.title("Convertidor de Python a C++")
root.geometry("1200x1000")  # Ajustar el tamaño de la ventana
root.resizable(False, False)

# Obtener el tamaño de la pantalla
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calcular la posición x e y para centrar la ventana
x = (screen_width // 2) - (1200 // 2)
y = (screen_height // 2) - (1000 // 2)

# Posicionar la ventana en el centro de la pantalla
root.geometry(f"1200x1000+{x}+{y}")

# Contenedor principal
frame_main = ttk.Frame(root, padding=20)
frame_main.pack(fill=BOTH, expand=YES)

# Crear un subframe para organizar los cuadros de texto en columnas
frame_text = ttk.Frame(frame_main)
frame_text.pack(fill=BOTH, expand=YES)

# Etiqueta de entrada y caja de texto para el código Python (columna izquierda)
label_input = ttk.Label(frame_text, text="Ingresa tu código Python:", font=("Helvetica", 14))
label_input.grid(row=0, column=0, padx=10, pady=5, sticky="w")

text_input = ttk.Text(frame_text, height=40, width=70)
text_input.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Etiqueta de salida y caja de texto para el código C++ (columna derecha)
label_output = ttk.Label(frame_text, text="Resultado en C++:", font=("Helvetica", 14))
label_output.grid(row=0, column=1, padx=10, pady=5, sticky="w")

text_output = ttk.Text(frame_text, height=40, width=70, state="disabled", bg="#f8f9fa")
text_output.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

# Configurar el grid para que las columnas se expandan igualmente
frame_text.columnconfigure(0, weight=1)
frame_text.columnconfigure(1, weight=1)

# Botón de conversión en el centro, debajo de los cuadros de texto
button_convertir = ttk.Button(frame_main, text="Convertir a C++", command=convertir, bootstyle="primary")
button_convertir.pack(pady=20)

# Ejecutar la interfaz
root.mainloop()
