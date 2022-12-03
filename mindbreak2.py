from tkinter import*

def secundaria():
    ventana_principal.destroy()
    global ventana_secundaria, fram_conf, framesec
    ventana_secundaria=Toplevel()
    ventana_secundaria.geometry("417x617")
    ventana_secundaria.config(bg="#eeeee4")
    ventana_secundaria.resizable(0,0)
    #frameconfig
    fram_conf=Frame(ventana_secundaria)
    fram_conf.config(bg="#eeeee4" ,width=417,height=617)
    fram_conf.place(x=0,y=0)
    #imagen
    cerebro=PhotoImage(file="imagenes/cerebro.png")
    lb_cerebro=Label(fram_conf, image=cerebro)
    lb_cerebro.config(bg="#eeeee4",)
    lb_cerebro.place(x=100, y=30)
    #frameavisual
    framesec=Frame(ventana_secundaria)
    framesec.config(bg="#eeeee4" ,width=417,height=417)
    framesec.place(x=0,y=260)
    #logos imagenes
    faceb=PhotoImage(file="imagenes/facebook.png")
    lb_faceb=Button(framesec, image=faceb)
    lb_faceb.config(bg="#eeeee4",bd=0)
    lb_faceb.place(x=30, y=75)
    twiter=PhotoImage(file="imagenes/twiter.png")
    lb_twiter=Button(framesec, image=twiter)
    lb_twiter.config(bg="#eeeee4",bd=0)
    lb_twiter.place(x=30, y=-3)
    instagram=PhotoImage(file="imagenes/instagram.png")
    lb_insta=Button(framesec, image=instagram)
    lb_insta.config(bg="#eeeee4",bd=0)
    lb_insta.place(x=30, y=145)
    tktok=PhotoImage(file="imagenes/tiktok.png")
    lb_tik=Button(framesec, image=tktok)
    lb_tik.config(bg="#eeeee4",bd=0)
    lb_tik.place(x=30, y=225)
    menu= PhotoImage(file="imagenes/list.png")
    botton= Button(fram_conf, image=menu)
    botton.config(bg="#eeeee4",bd=0)
    botton.place(x=0,y=0)
    
    ventana_secundaria.mainloop()

ventana_principal = Tk()
ventana_principal.title("MINDBREAK")
ventana_principal.geometry("417x617")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="#eeeee4")
#imagen
imagen= PhotoImage(file="imagenes/tl.png")
imagen_logo = PhotoImage(file="imagenes/titulo.png")
imagen_portada = PhotoImage(file="imagenes/portada.png")
#buttoninicio
lb_logo = Label(image=imagen_logo)
lb_logo.place(x=10, y=10 )
lb_logo.config(width=397, height=200, bg="#eeeee4")

boton = Button(image=imagen, text="ACCEDER",command=secundaria)
boton.place(x=160, y=220)
boton.config(width=100, height=100, bg="#eeeee4", bd=0,cursor="hand2")

lb_por = Label(image=imagen_portada)
lb_por.place(x=108, y=330 )
lb_por.config(width=200, height=200, bg="#eeeee4")

etiqueta = Label(text="Creado por: \n Estévez Cárdenas Jose Fernando\n Olarte Saavedra Shneider Alejandro \n UIS\n")
etiqueta.config(bg="#eeeee4")
etiqueta.pack(side="bottom", pady=5)

ventana_principal.mainloop()
