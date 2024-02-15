from tkinter import *
window=Tk()
window.geometry('300x300')

#frame'de kullanılacakk özellikler
#height,widht,background,highlightbackground(çerçeve rengi),highlightthickness(çerçeve kalınlığı,piksel),cursor(imleç şekli),padx,pady
#cursor types:
#"arrow","circle","clock","cross","dotbox","exchange","fleur","heart","heart","man","mouse","pirate","plus","shuttle","sizing","spider","spraycan","star","target","tcross","trek","watch"
frame1=Frame(window,height=50,width=100,bg='green',highlightbackground='red',highlightthickness=4,cursor="pirate", padx=10,pady=20)
frame1.pack()
frame2=Frame(window,height=50,width=100,bg='yellow',highlightbackground='pink',highlightthickness=4,cursor="man")
frame2.pack()

label1=Label(frame1,text='label1')
label1.place(x=0,y=0)
label2=Label(frame2,text='label2')
label2.place(x=0,y=0)
#padx ve pady içlerine gelen etiketlerin çerçeveye mesafelerini belirler.padx=10 pady=30 dendiğinde 10 piksel sağdan 30 piksel yyukarıdan boşluk bırakarak yazar
window.mainloop()
