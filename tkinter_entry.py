from tkinter import *
window=Tk()
window.geometry('400x800')
#ENTRY PARAMETRELERİ
#font,bg,fg,bd(border,kenar kalınlığı),width,cursor,relief,show,justify,selectbackgroung,selectborderwidth,selectforeground,state(disabled,normal),textvariable
#hight, fontun puntosudur
#ENTRY METODS
#get(),delete(), insert(index,s) , select_to(index) , select_range(start,end) , select_present() , icursor(index)

Entry(window,font=('Arial 10 bold underline'),bg='yellow',fg='black',bd=2,width=30,cursor='spider').pack()

Entry(window,relief=FLAT).pack(pady=10)        #eğer pady entry içinde yazarsak çerçevesi ve stringi arasında boşluk bırakır, pack içinde yazarsak kendinden sonraki objeyle arasında boşluk bırakır
Entry(window,relief=RAISED).pack(pady=10)
Entry(window,relief=SUNKEN).pack(pady=10)
Entry(window,relief=GROOVE).pack(pady=10)
Entry(window,relief=RIDGE).pack(pady=10)
# Entry(window,relief=RIDGE).pack()
# Entry(window,relief=RIDGE).pack()
# Entry(window,relief=RIDGE).pack()
# Entry(window,relief=RIDGE).pack()
# Entry(window,relief=RIDGE).pack()

Entry(window,show='*',bg='blue').pack()           #şifrenin görünmemesi

Entry(window,justify='right',bg='red').pack()       #yazının hangi yönden yazılacağı , defaultu left

Entry(window,selectbackground='green',selectborderwidth=15,selectforeground='brown').pack()
#sbg:seçildiğinde arkaplan rengi   sbw:seçildiğinde imleç boyutu  sfg:seçildiğinde yazı rengi

Entry(window,bg='black',fg='white',state='disabled').pack()     #renkleri kapattı,yazmayı da

halihazır=StringVar(window,value='Random Text')
Entry(window,textvariable=halihazır).pack(pady=10)             #metin açılan ekranda gelsin

#METODS
entry=Entry(window)
entry.pack()
entry2=Entry(window)
entry2.pack()
entry3=Entry(window)
entry3.pack()
entry4=Entry(window)
entry4.pack()
entry5=Entry(window)
entry5.pack()
entry6=Entry(window)
entry6.pack()
entry7=Entry(window)
entry7.pack()
def clicked_button():
    print(entry.get())      #entry'yazılmış yazıyı terminale bastırır
def clicked_button2():
    entry2.delete(0,'end')      #index aralığı verilir, verilen aralığı siler
def clicked_button3():
    entry3.insert(7,'salağım')    #ıncı indexten başla ve şunu yaz, kalan indextekileri kaydırıyor
def clicked_button4():
    entry4.select_to(3)         #imlecin bulunduğu konumdan indexe kadar seç
def clicked_button5():
    entry5.select_range(3,6)        #bu iki index arasını seç
def clicked_button6():
    print(entry6.select_present())     #entry'de seçili karakter varsa true, yoksa false döner
def clicked_button7():
    entry7.icursor(5)           #imleci şu indexe götür

Button(window,text='get',command=clicked_button).pack(pady=10)
Button(window, text='delete', command=clicked_button2).pack(pady=10)
Button(window, text='insert', command=clicked_button3).pack(pady=10)
Button(window,text='select_to',command=clicked_button4).pack(pady=10)
Button(window, text='select_range', command=clicked_button5).pack(pady=10)
Button(window, text='select_present', command=clicked_button6).pack(pady=10)
Button(window, text='icursor', command=clicked_button7).pack(pady=10)

window.mainloop()



#reshide bi şeyler deniyor
"""
def clicked_button():
    metods=[entry.get(),entry.delete(0,'end'),entry.select_to(3),entry.select_range(3,9),entry.select_present(),entry.icursor(5)]
    for i in range(len(metods)):
        return metods[i]
    i+=1

Button(window,text='hello metods',command=clicked_button).pack(pady=10)
"""