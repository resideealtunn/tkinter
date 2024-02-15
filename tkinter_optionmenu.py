from tkinter import *

#option list , font, bg, fg, cursor, width, height, padx, pady, anchor, relief, image, compound
#get() , set()
window=Tk()
window.geometry('400x1000')

sval=StringVar(value='sayı')
OptionMenu(window,sval,'18','19','20').pack()

#optionlist
optionlist= ['Ocak','Şubat','Mart','Nisan','Mayıs','Haziran']
sval2=StringVar(value='aylar')      #value=optionlist[0]
OptionMenu(window,sval2,*optionlist).pack()

#CONFİG(yapılandırma)
optionlist3= ['Ocak','Şubat','Mart','Nisan','Mayıs','Haziran']
sval3=StringVar(value=optionlist3[0])
opm1=OptionMenu(window,sval3,*optionlist3)
opm1.config(font=('Times 10 bold'),bg='lightblue',fg='red',cursor='spider',width=20,height=4)
opm1.pack()

optionlist4= ['Ocak','Şubat','Mart','Nisan','Mayıs','Haziran']
sval4=StringVar(value=optionlist4[0])
opm2=OptionMenu(window,sval4,*optionlist4)
opm2.config(font=('Times 10 bold'),bg='lightblue',fg='red',cursor='spider',width=20,height=4,pady=50,padx=50)
opm2.pack()

optionlist5= ['Ocak','Şubat','Mart','Nisan','Mayıs','Haziran']
sval5=StringVar(value=optionlist5[0])
opm3=OptionMenu(window,sval5,*optionlist5)
photo=PhotoImage(file='person.png')
photoresized=photo.subsample(5,5)       #width ve hight işi bozuyor
opm3.config(font=('Times 10 bold'),bg='lightblue',fg='red',cursor='spider',anchor='sw',relief=SUNKEN,image=photoresized,compound=LEFT)
opm3.pack()

#reshide trying something - seçimle foto degistirme - get()
optionlist3= ['Ocak','Şubat','Mart','Nisan','Mayıs','Haziran']
sval3=StringVar(value=optionlist3[0])
opm1=OptionMenu(window,sval3,*optionlist3)
photo=PhotoImage(file='person.png')
photoresized=photo.subsample(5,5)
opm1.config(font=('Times 10 bold'),bg='lightblue',fg='red',cursor='spider',image=photoresized,compound=LEFT)
opm1.pack()
def clicked_button():
    veri=sval3.get()
    print(veri)
    if veri == 'Mayıs':
        photo2=PhotoImage(file='vangogh.png')
        photoresized2=photo2.subsample(5,5)
        opm1.config(font=('Times 10 bold'), bg='lightblue', fg='red', cursor='spider', image=photoresized2,
                    compound=LEFT).pack()
Button(window,text='buton',command=clicked_button).pack()

#set()
svalx=StringVar()
svalx.set(optionlist[0]
#StringVar() içine yazmak yerine böyle de kullanılabilir

window.mainloop()
