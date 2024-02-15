from tkinter import *
#tearoff, font, bg, fg, activebackground, activeforeground
#add_command(options), add_cascade(options), add_seperator(), add_checkbutton(options), add_radiobutton(options)
window=Tk()
window.geometry('300x300')

def donothing():
    print('yes ay dozont')
    #eğer buraya dosya işlemleri yazarsak gerçek bir uygulamaya dönüştürebiliriz
menubar=Menu(window)
filemenu=Menu(menubar)#menübarın alt seçeneklerini oluşturduk
filemenu2=Menu(menubar,tearoff=0,font='Times 12 italic',bg='lightgreen',fg='orange',activebackground='gray',activeforeground='red')
menubar.add_cascade(label='File',menu=filemenu)
menubar.add_cascade(label='File2',menu=filemenu2)
filemenu.add_command(label='New')
filemenu2.add_command(label='Search',command=donothing)
filemenu2.add_command(label='Open',command=donothing)
filemenu2.add_command(label='Close',command=donothing)
filemenu2.add_separator()       #araya çizgi çizmeye yarıyor
filemenu2.add_command(label='Delete',command=donothing)
filemenu2.add_checkbutton(label='checkbutton',command=donothing)
filemenu2.add_radiobutton(label='radiobutton',command=donothing)
filemenu2.add_radiobutton(label='radiobutton2',command=donothing)


window.config(menu=menubar) #menu(window) çalışması için gerekli, yukarıdaki ilk menüyü oluşturduk
window.mainloop()