import tkinter as tk

# ventana
ventana = tk.Tk() 
ventana.title("Convertidor de horas a segundos") 
ventana.geometry("350x200")

# etiqueta
etiqueta = tk.Label(ventana, text="Introduzca las horas y los minutos:") 
etiqueta.grid(column=0, row=0) 

# variables
hora_valor = tk.StringVar() 
minuto_valor = tk.StringVar()

# campo de horas
hora_campo = tk.Entry(ventana, width=5, textvariable=hora_valor) 
hora_campo.grid(column=1, row=0) 

# etiqueta minutos
minuto_etiqueta = tk.Label(ventana, text="Minutos:") 
minuto_etiqueta.grid(column=2, row=0) 

# campo de minutos
minuto_campo = tk.Entry(ventana, width=5, textvariable=minuto_valor) 
minuto_campo.grid(column=3, row=0) 

# etiqueta resultado
resultado_etiqueta = tk.Label(ventana, text="Resultado:") 
resultado_etiqueta.grid(column=0, row=2) 

# etiqueta de resultado
resultado = tk.Label(ventana, text="") 
resultado.grid(column=2, row=2)

# función de conversión
def convertir(): 
	hora = int(hora_valor.get()) 
	minuto = int(minuto_valor.get()) 
	
	segundos = hora * 3600 + minuto * 60
	
	resultado.configure(text= str(segundos) + " segundos")

# botón
boton = tk.Button(ventana, text="Convertir", command=convertir) 
boton.grid(column=3, row=1)

ventana.mainloop()