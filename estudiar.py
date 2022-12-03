import time

tiempo = int(input('¿Cuánto tiempo deseas que dure el temporizador (en segundos)? '))

for x in range(tiempo):
    print(tiempo - x)
    time.sleep(1)

print('¡El tiempo ha terminado!')

from tkinter import *
import tkinter as tk
from tkinter import messagebox

# Función principal# Crear la ventana
window = tk.Tk()
window.title('Temporizador')
# Crear etiquetas
label_tiempo = tk.Label(window, text='Introduce el tiempo (en segundos):')
label_tiempo.grid(row=0, column=0, padx=5, pady=5)
# Crear entrada de texto
entry_tiempo = tk.Entry(window)
entry_tiempo.grid(row=0, column=1, padx=5, pady=5)

# Crear botón
boton_iniciar = tk.Button(window, text='Iniciar', command=lambda: iniciar_temporizador(window, entry_tiempo))
boton_iniciar.grid(row=1, column=0, padx=5, pady=5)

window.mainloop()