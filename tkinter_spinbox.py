from tkinter import *

#skills; from_ , to, increment, font, bg, fg, cursor, bd, width, justify, relief, state, textvariable, command, disabledbackground, disabledforeground,format
#metods; get()
#from_ , to şu sayıdan şu sayıya kadar seçim hakkı tanı
#increment her basışta artış miktarı
window=Tk()
window.geometry('400x300')

Spinbox(window,from_=1,to=31, increment=3,font=('Times 8 bold'),bg='yellow',foreground='red',cursor='dotbox',bd=3,width=10,justify='center',relief=GROOVE,state='normal').pack()
Spinbox(window,from_=1,to=31, increment=3,font=('Times 8 bold'),bg='yellow',foreground='red',cursor='dotbox',bd=3,width=10,justify='center',relief=GROOVE,state='disabled').pack()
Spinbox(window,from_=1,to=31, increment=3,font=('Times 8 bold'),bg='yellow',foreground='red',cursor='dotbox',bd=3,width=10,justify='center',relief=GROOVE,state='disabled',disabledbackground='orange',disabledforeground='black').pack()

svar=StringVar(value='23')
Spinbox(window,from_=1,to=31, increment=3,font=('Times 8 bold'),bg='yellow',foreground='red',cursor='dotbox',bd=3,width=10,justify='center',relief=GROOVE,state='normal',textvariable=svar).pack()

def changed_value():
    print(spinb.get())      #get değişen her değeri terminale bastırır
spinb=Spinbox(window,from_=1,to=31, increment=3,font=('Times 8 bold'),bg='yellow',foreground='red',cursor='dotbox',bd=3,width=10,justify='center',relief=GROOVE,command=changed_value)
spinb.pack()

#format sayıyı hangi formatta kaç basamaklı görmek istediğimizi yazarız
Spinbox(window,from_=89,to=1131, increment=3.5,font=('Times 8 bold'),bg='yellow',foreground='red',cursor='dotbox',bd=3,width=10,justify='center',relief=GROOVE, format='%02.03f').pack()

window.mainloop()