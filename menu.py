import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Temporizador")

# Función que cuenta el tiempo
def contador():
    segundos = int(entry_segundos.get())
    for segundo in range(segundos):
        print(segundo + 1)
        ventana.update()
        ventana.after(1000)
    messagebox.showinfo(title="Fin", message="Ha finalizado el temporizador")

# Frame
frame = tk.Frame(ventana)
frame.pack()

# Label
label_segundos = tk.Label(frame, text="Segundos:")
label_segundos.grid(row=0, column=0, padx=5, pady=5)

# Entry
entry_segundos = tk.Entry(frame)
entry_segundos.grid(row=0, column=1, padx=5, pady=5)

# Botón
boton_iniciar = tk.Button(frame, text="Iniciar", command=contador)
boton_iniciar.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

ventana.mainloop()