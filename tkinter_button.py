from tkinter import *
window=Tk()
window.geometry('600x600')

#kullanılacak özellikler
#text,font,bg,fg, activebackground, activeforeground , cursor, height, width, wraplength, bd ,command, padx, pady,relief,state, immage,compound
#activebackground,afg = tıklandığında yazı ve arkaplan rengi
Button(window,text='Click me!',font=('Times 15 bold italic'),bg='lightgreen',fg='red',activebackground='green',activeforeground='pink',cursor="watch",width=30,height=3,bd=56).pack()

#command , tuşladığında  yapılacak işlemi,fonksiyonu yaz
def command_fonk():
    print('hello command!')
Button(window,text='Click me!',font=('Helvetica 15'),command=command_fonk).pack()

#pack'in içine padx,pady yazarsan butonlar arasına ; button içine yazarsan yazı ile buton arasına boşluk verir!!!

reliefList=[FLAT,RAISED,SUNKEN,GROOVE,RIDGE]
for reliefItem in reliefList:
    Button(window,text='hello relief!',relief=reliefItem).pack(pady=5)

#image,compound
photo=PhotoImage(file='vangogh.png')
resizedphoto=photo.subsample(8,8)       #sayı büyüdükçe küçülüyor
Button(window,text='hello van gogh',image=resizedphoto,compound=LEFT).pack()
window.mainloop()