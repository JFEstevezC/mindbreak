from tkinter import*

def aceptar():
    usuario = usuario_entry.get()
    if usuario:
        etiqueta.configure(text="Usuario: " + usuario)
    else:
        etiqueta.configure(text="Usuario no introducido")
        ventana_de_configuracion.destroy()
    
def cancelar():
    usuario_entry.delete(0, "end")
    contraseña_entry.delete(0, "end")

def inicio():
    global ventana_de_configuracion, usuario_entry, contraseña_entry
    
    ventana_de_configuracion = Toplevel()
    ventana_de_configuracion.title("Configuración")
    ventana_de_configuracion.resizable(False, False)

    usuario_label = Label(ventana_de_configuracion, text="USUARIO:")
    usuario_entry = Entry(ventana_de_configuracion, bd=5, highlightcolor="red", highlightthickness=2)
    contraseña_label = Label(ventana_de_configuracion, text="CONTRASEÑA:")
    contraseña_entry = Entry(ventana_de_configuracion, bd=5, show='*', highlightcolor="red", highlightthickness=2)
    boton_aceptar = Button(ventana_de_configuracion, text="ACEPTAR", command=aceptar)
    boton_cancelar = Button(ventana_de_configuracion, text="CANCELAR", command=cancelar)

    usuario_label.grid(row=0, column=0, sticky= "W", padx=10, pady=10)
    usuario_entry.grid(row=0, column=1, padx=10)
    contraseña_label.grid(row=1, column=0, sticky= "W", padx=10, pady=10)
    contraseña_entry.grid(row=1, column=1, padx=10)
    boton_aceptar.grid(row=2, column=0, padx=10, pady=10, sticky= "W")
    boton_cancelar.grid(row=2, column=1, padx=10, pady=10, sticky= "E")

ventana_principal = Tk()
ventana_principal.title("MINDBREAK")
ventana_principal.geometry("417x627")
ventana_principal.minsize(417, 627)
ventana_principal.config(bg="#eeeee4")
#imagen
imagen= PhotoImage(file="imagenes/tl.png")
#buttoninicio
boton = Button(image=imagen, text="ACCEDER",command=inicio)
boton.config(width=180, height=180, bg="#eeeee4", bd=0,cursor="hand2")
etiqueta = Label(text="Usuario no introducido")
boton.place(relx=0.27, rely=0.18, )
etiqueta.pack(side="bottom", pady=5)

ventana_principal.mainloop()
