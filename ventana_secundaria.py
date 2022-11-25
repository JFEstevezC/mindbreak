from tkinter import*
#ventasecundaria
BASE=417
ALTURA=617
c="#eeeee4"
ventana_secundaria=Tk()
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
lb_faceb=Label(framesec, image=faceb)
lb_faceb.config(bg=c,)
lb_faceb.place(x=30, y=58)

twiter=PhotoImage(file="imagenes/twiter.png")
lb_twiter=Label(framesec, image=twiter)
lb_twiter.config(bg=c,)
lb_twiter.place(x=30, y=-20)

instagram=PhotoImage(file="imagenes/instagram.png")
lb_insta=Label(framesec, image=instagram)
lb_insta.config(bg=c,)
lb_insta.place(x=30, y=137)

tktok=PhotoImage(file="imagenes/tiktok.png")
lb_tik=Label(framesec, image=tktok)
lb_tik.config(bg=c,)
lb_tik.place(x=30, y=225)


ventana_secundaria.mainloop()
