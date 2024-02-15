from tkinter import *
#text, font, bg, fg, activebackground, activeforeground,height,wight,padx,pady,wraplength,cursor,anchor,state, relief, image,variable,command,offvalue,onvalue
#metodlar(metod kullanmak için obje tanımlammak gerek)
#select, deselect, toggle
window=Tk()
window.geometry('400x900')

Checkbutton(window,text='checkbox widget',font='Times 12 bold',bg='lightblue',fg='black',
            activeforeground='lightblue', activebackground='black',height=3,width=30,
            cursor='spider',anchor='n',state=DISABLED,relief=SUNKEN).pack()

Checkbutton(window,text='checkbox widget 2',font='Times 12 bold',bg='red',fg='pink',
            activeforeground='lightblue', activebackground='black',height=3,width=30,padx=10,pady=10).pack()

Checkbutton(window,text='checkbox widget',font='Times 12 bold',bg='lightblue',fg='black',
            activeforeground='lightblue', activebackground='black',height=8,width=30,
            wraplength=30).pack()
#wraplenght : 30 piksele sığacak kadar karakter alır kalanı alt satıra geçirri


photo=PhotoImage(file='vangogh.png')
photoresized=photo.subsample(8,8)     #12de birine düşür
Checkbutton(window,text='checkbox widget 2',font='Times 12 bold',bg='red',fg='pink',
            activeforeground='lightblue', activebackground='black',image=photoresized).pack()

ivar=IntVar()
def sel():
    selection= 'clicked checkbox val=' + str(ivar.get())
    print(selection)
Checkbutton(window,text='checkbox widget',font='Times 12 bold',bg='lightblue',fg='black',
            activeforeground='lightblue', activebackground='black',height=3,width=30,
            variable=ivar,command=sel,onvalue=4,offvalue=5).pack()       #variable commandla beraber kullanılıyor, default'u 1 ve 0 - dedğiştirmek için onvalue ve offvalue

chb1=Checkbutton(window,text='checkbox widget 2',font='Times 12 bold',bg='red',fg='pink',
            activeforeground='lightblue', activebackground='black',height=3,width=30)
chb1.pack()
chb1.select()   #checkbox'ıtikli getirir
#chb1.toggle ; tikliyse tikini kaldırır, tiksizse tikler


window.mainloop()