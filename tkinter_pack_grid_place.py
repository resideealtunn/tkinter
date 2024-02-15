from tkinter import *

window=Tk()
window.geometry('400x400')

label1= Label(window, text='label1')
label2= Label(window, text='label2')
label3= Label(window, text='label3')
label4= Label(window, text='label4')

#pack,grid ve place direkt label tanımının sonuna yazılabilir;
#label1= Label(window, text='label1').pack() vb.


#pack
"""
label1.pack(side=TOP)           #default'u ortalayıp yukarıya dayamaktır
label2.pack(side=LEFT)
label3.pack(side=RIGHT)
label4.pack(side=BOTTOM)
"""

#grid
"""
label1.grid(column=0,row=0)     #fark atıldığında atılmamış gibi boş yeri doldurur
label2.grid(column=0,row=1)
label3.grid(column=0,row=2)
label4.grid(column=0,row=10)
"""

#place
label1.place(x=100,y=45)
label2.place(x=100,y=90)
label3.place(x=100,y=135)
label4.place(x=100,y=180)


window.mainloop()