from tkinter import*
<<<<<<< HEAD
c="#eeeee4"   
def secundaria():
     global ventana_secundaria, fram_conf, framesec
     ventana_secundaria=Toplevel()
     ventana_secundaria.geometry("417x617")
     ventana_secundaria.config(bg=c)
     ventana_secundaria.resizable(0,0)
     #frameconfig
     fram_conf=Frame(ventana_secundaria)
     fram_conf.config(bg=c ,width=417,height=617)
     fram_conf.place(x=0,y=0)
     #imagen
     cerebro=PhotoImage(file="imagenes/cerebro.png")
     lb_cerebro=Label(fram_conf, image=cerebro)
     lb_cerebro.config(bg=c,)
     lb_cerebro.place(x=100, y=30)
     #frameavisual
     framesec=Frame(ventana_secundaria)
     framesec.config(bg=c ,width=417,height=417)
     framesec.place(x=0,y=260)
     #logos imagenes
     faceb=PhotoImage(file="imagenes/facebook.png")
     lb_faceb=Button(framesec, image=faceb)
     lb_faceb.config(bg=c,bd=0)
     lb_faceb.place(x=30, y=75)
     twiter=PhotoImage(file="imagenes/twiter.png")
     lb_twiter=Button(framesec, image=twiter)
     lb_twiter.config(bg=c,bd=0)
     lb_twiter.place(x=30, y=-3)
     instagram=PhotoImage(file="imagenes/instagram.png")
     lb_insta=Button(framesec, image=instagram)
     lb_insta.config(bg=c,bd=0)
     lb_insta.place(x=30, y=145)
     tktok=PhotoImage(file="imagenes/tiktok.png")
     lb_tik=Button(framesec, image=tktok)
     lb_tik.config(bg=c,bd=0)
     lb_tik.place(x=30, y=225)
     menu= PhotoImage(file="imagenes/list.png")
     botton= Button(fram_conf, image=menu)
     botton.config(bg=c,bd=0)
     botton.place(x=0,y=0)

     ventana_secundaria.mainloop()
    
ventana_principal =Tk()
=======

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

    usuario_label = Label(ventana_acceso, text="USUARIO:")
    usuario_entry = Entry(ventana_acceso, bd=5, highlightcolor="red", highlightthickness=2)
    contraseña_label = Label(ventana_acceso, text="CONTRASEÑA:")
    contraseña_entry = Entry(ventana_acceso, bd=5, show='*', highlightcolor="red", highlightthickness=2)
    boton_aceptar = Button(ventana_acceso, text="ACEPTAR", command=aceptar)
    boton_cancelar = Button(ventana_acceso, text="CANCELAR", command=cancelar)

    usuario_label.grid(row=0, column=0, sticky= "W", padx=10, pady=10)
    usuario_entry.grid(row=0, column=1, padx=10)
    contraseña_label.grid(row=1, column=0, sticky= "W", padx=10, pady=10)
    contraseña_entry.grid(row=1, column=1, padx=10)
    boton_aceptar.grid(row=2, column=0, padx=10, pady=10, sticky= "W")
    boton_cancelar.grid(row=2, column=1, padx=10, pady=10, sticky= "E")

ventana_principal = Tk()
>>>>>>> ceed74c96b1e40592e0e5c5317492bc09138dfc0
ventana_principal.title("MINDBREAK")
ventana_principal.geometry("417x627")
ventana_principal.minsize(417, 627)
ventana_principal.config(bg=c)
#imagen
imagen= PhotoImage(file="imagenes/tl.png")
#buttoninicio
boton = Button(image=imagen, text="ACCEDER",command=secundaria)
boton.config(width=180, height=180, bg="#eeeee4",cursor="hand2",bd=0)
etiqueta = Label(text="Usuario no introducido")
boton.place(relx=0.27, rely=0.18, )
etiqueta.pack(side="bottom", pady=5)

ventana_principal.mainloop()
