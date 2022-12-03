from tkinter import*
c="#eeeee4"
def configuracion():
    
    ter_vent=Toplevel()
    ter_vent.geometry("417x617+540+10")
    ter_vent.resizable(0,0)
    ter_vent.config(bg=c)
    #button
    engr=PhotoImage(file="imagenes/engranaje.png")
    bt_engr=Button(ter_vent, image=engr, command=secundaria)
    bt_engr.config(bg=c, bd=0)
    bt_engr.place(x=0,y=0)

    mas=PhotoImage(file="imagenes/mas.png")
    bt_mas=Button(ter_vent, image=mas,)
    bt_mas.config(bg=c, bd=0)
    bt_mas.place(x=220,y=280)

    menos=PhotoImage(file="imagenes/menos.png")
    bt_menos=Button(ter_vent, image=menos,)
    bt_menos.config(bg=c, bd=0)
    bt_menos.place(x=270,y=280)

    reloj=PhotoImage(file="imagenes/reloj.png")
    lb_reloj=Label(ter_vent, image=reloj)
    lb_reloj.config(bg=c,)
    lb_reloj.place(x=125,y=60)


    lb_tiempo=Label(ter_vent, text="Tiempo límite")
    lb_tiempo.config(bg="#eeeee4",width=30, height=40, fg="blue", font=("Arial", 12))
    lb_tiempo.place(x=100, y=300)

    #checklist
    list=Checkbutton(ter_vent,text="")
    list.config(bg=c, )
    list.place(x=220, y=350)
    
    #checklist
    list=Checkbutton(ter_vent,text="")
    list.config(bg=c, )
    list.place(x=220, y=400)
    
    #checklist
    list=Checkbutton(ter_vent,text="")
    list.config(bg=c, )
    list.place(x=220, y=450)
    ter_vent.mainloop()


def secundaria():
    global ventana_secundaria, fram_conf, framesec
    ventana_secundaria=Toplevel()
    ventana_secundaria.geometry("417x617+540+10")
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
    info=PhotoImage(file="imagenes/simboloinfo.png")
    lb_faceb=Label(framesec, image=faceb)
    lb_faceb.config(bg="#eeeee4",bd=0)
    lb_faceb.place(x=30, y=75)
    lb_faceb1=Label(framesec, text= "Tiempo de uso")
    lb_faceb1.config(bg="#eeeee4", fg="black", font=("Arial",16))
    lb_faceb1.place(x=100, y=75)
    lb_info1=Label(framesec, image=info)
    lb_info1.config(bg="#eeeee4", fg="black", font=("Arial",16))
    lb_info1.place(x=300, y=75)
    twiter=PhotoImage(file="imagenes/twiter.png")
    lb_twiter=Label(framesec, image=twiter)
    lb_twiter.config(bg="#eeeee4",bd=0)
    lb_twiter.place(x=30, y=-3)
    lb_twiter1=Label(framesec, text= "Tiempo de uso")
    lb_twiter1.config(bg="#eeeee4", fg="black", font=("Arial",16))
    lb_twiter1.place(x=100, y=-3)
    lb_info2=Label(framesec, image=info)
    lb_info2.config(bg="#eeeee4", fg="black", font=("Arial",16))
    lb_info2.place(x=300, y=-3)
    instagram=PhotoImage(file="imagenes/instagram.png")
    lb_insta=Label(framesec, image=instagram)
    lb_insta.config(bg="#eeeee4",bd=0)
    lb_insta.place(x=30, y=145)
    lb_insta1=Label(framesec, text= "Tiempo de uso")
    lb_insta1.config(bg="#eeeee4", fg="black", font=("Arial",16))
    lb_insta1.place(x=100, y=145)
    lb_info3=Label(framesec, image=info)
    lb_info3.config(bg="#eeeee4", fg="black", font=("Arial",16))
    lb_info3.place(x=300, y=145)
    tktok=PhotoImage(file="imagenes/tiktok.png")
    lb_tik=Label(framesec, image=tktok)
    lb_tik.config(bg="#eeeee4",bd=0)
    lb_tik.place(x=30, y=225)
    lb_tik1=Label(framesec, text= "Tiempo de uso")
    lb_tik1.config(bg="#eeeee4", fg="black", font=("Arial",16))
    lb_tik1.place(x=100, y=225)
    lb_info4=Label(framesec, image=info)
    lb_info4.config(bg="#eeeee4", fg="black", font=("Arial",16))
    lb_info4.place(x=300, y=225)

    menu= PhotoImage(file="imagenes/list.png")
    botton= Button(fram_conf, image=menu, command=configuracion)
    botton.config(bg="#eeeee4",bd=0)
    botton.place(x=0,y=0)
    
    ventana_secundaria.mainloop()



ventana_principal = Tk()
ventana_principal.title("MINDBREAK")
ventana_principal.geometry("417x617+540+10")
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
