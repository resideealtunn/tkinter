from tkinter import *
window=Tk()
window.geometry('800x800')

#label skills
#text,font,bg,foreground(fg),cursor,height(karakter),widht(karakter),wraplenght(piksel),padx,pady,anchor(yön),relief(çerçeve şekli),bitmap,image,compound
#window yerine labeli(etiketi) nerede görmek istediğimizi yazarız
#font birden çok parametre alabildiğinden parantez içinde yazılmalıdır
#wraplenght; genişliği piksel cinsinden verir, sığmazsa alt satıra geçirir
#anchor; N:kuzey(north) W:batı(west) E:doğu(east) S:güney(south) nw:kuzeybatı ne:kuzeydoğu sw:güneybatı se:güneydoğu
#relief mods; FLAT , RAISED , SUNKEN , GROOVE , RIDGE
#bitmap icons;"error","gray75","gray50","gray25","gray12","hourglass","info","questhead","question","warning"

Label(window,text='Python Tk Label',font=('Arial',10),bg='green',fg='red',cursor='spider',width=10,height=8,wraplength=120).pack()

Label(window,text='Python tk label',font=('Helvetica 12 bold italic underline')).pack()

Label(window,text='padx pady',font=('Times',15),bg='red').pack()
Label(window,text='padx pady',font=('Times',15),bg='red',padx=10,pady=10).pack()

Label(window,text='anchor',font=('Helvetica',15),bg='blue',height=1,width=10).pack()
Label(window,text='anchor',font=('Helvetica',15),bg='blue',height=1,width=10,anchor='w').pack()

Label(window,text='relief',font=('Times',15),relief=FLAT).pack()
Label(window,text='relief',font=('Times',15),relief=RAISED).pack()
Label(window,text='relief',font=('Times',15),relief=SUNKEN).pack()
Label(window,text='relief',font=('Times',15),relief=GROOVE).pack()
Label(window,text='relief',font=('Times',15),relief=RIDGE).pack()

Label(window,text='bitmaps',font=('Times',15),bitmap="error").pack()    #bitmap text'i yutar

photo=PhotoImage(file="vangogh.png")
photoResized=photo.subsample(8,8)       #fotonun boyutunu ayarladık
Label(window,text='fotograf',font=('Arial',15),image=photoResized).pack()
#resmin konumunu compound belirler
Label(window,text='fotograf',font=('Arial',15),image=photoResized,compound=RIGHT).pack()

window.mainloop()