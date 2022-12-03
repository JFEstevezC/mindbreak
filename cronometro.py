import tkinter as tk
from tkinter import ttk

# creamos la ventana
ventana = tk.Tk()
ventana.title("Temporizador")
ventana.geometry("300x150")

# creamos la etiqueta
etiqueta = ttk.Label(ventana, text="Introduce el número de minutos:")
etiqueta.grid(column=0, row=0)

# creamos el campo de entrada
minutos = tk.IntVar()
campo = ttk.Entry(ventana, width=10, textvariable=minutos)
campo.grid(column=1, row=0)

# creamos el botón
def iniciar():
    tiempo = minutos.get() *60
    for i in range(tiempo):
        tiempo = tiempo -1
        if tiempo == 0:
            print("¡Terminó el tiempo!")
            break

boton = ttk.Button(ventana, text="Iniciar", command=iniciar)
boton.grid(column=0, row=1)

ventana.mainloop()