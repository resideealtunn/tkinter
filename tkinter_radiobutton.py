from tkinter import *
#text, variable, value, font, bg, fg, activebackground, activeforeground,hheight,wight,padx,pady,wraplength,cursor,anchor,state, relief, image,command
#select , deselect
window=Tk()
window.geometry('400x500')

ivar=IntVar()
Radiobutton(window,text='Seçim 1' , variable=ivar,value=1).pack()
Radiobutton(window,text='Seçim 2', variable=ivar,value=2).pack()

Radiobutton(window,text='Seçim 3' , variable=ivar,value=3,font='Times 15 italic', bg='lightgreen', fg='gray',
            activebackground='red', activeforeground='white',height=3, width=25).pack()

Radiobutton(window,text='Seçim 4' , variable=ivar,value=4,font='Times 15 italic', bg='green', fg='gray',
            activebackground='red', activeforeground='white',height=3, width=25,padx=10,pady=10).pack()     #yazı ve çerçeve arası piksel boşluğu artırdık

def sel():
    selection='selected radiobutton val=' + str(ivar.get())
    print(selection)
Radiobutton(window,text='Seçim 5' , variable=ivar,value=5,font='Times 15 italic', bg='lightgreen', fg='gray',
            activebackground='red', activeforeground='white',height=3, width=25,wraplength=30,cursor='spider',
            anchor='nw',command=sel).pack()

Radiobutton(window,text='Seçim 6', variable=ivar,value=6,state=DISABLED,relief=SUNKEN).pack()

#EĞER RESİM EKLENİYORSA O RADYO BUTONUNUN BOYUTUNUN OYNANMAMASI(height ve weidth ) verilmemesi gerekir
photo=PhotoImage(file='vangogh.png')
photoresized=photo.subsample(14,14)
Radiobutton(window,text='Seçim 7' , variable=ivar,value=7,image=photoresized).pack()

rd8=Radiobutton(window,text='Seçim 8' , variable=ivar,value=1)
rd8.pack()
rd8.select()        #seçili gelsin diye
window.mainloop()