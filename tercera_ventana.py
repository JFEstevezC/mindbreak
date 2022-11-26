from tkinter import*
c="#eeeee4"
def volver():
    ter_vent.destroy()





ter_vent=Tk()
ter_vent.geometry("417x617")
ter_vent.resizable(0,0)
ter_vent.config(bg=c)
#button
engr=PhotoImage(file="imagenes/engranaje.png")
bt_engr=Button(ter_vent, image=engr, command=volver)
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

#checklist
list=Checkbutton(ter_vent,text="opcion" )
list.config(bg=c)
list.place(x=220, y=350)
ter_vent.mainloop()