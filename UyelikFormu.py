from tkinter import *
pencere=Tk()
pencere.title('Üyelik Formu')
pencere.geometry('450x400+750+200')
pencere.attributes('-topmost',1)
pencere.configure(bg='#FF9999')
#pencere.iconbitmap('people.ico')

frame1=Frame(pencere,bg='#FF9999')
frame1.grid(row=0,column=0)
frame2=Frame(pencere,bg='#FF9999')
frame2.grid(row=0,column=1)
frame3=Frame(pencere,bg='#FF9999')
frame3.grid(row=0,column=3)
frame4=Frame(pencere)
frame4.grid(row=1,column=3)
frame5=Frame(pencere,bg='#FF9999')
frame5.place(x=0,y=230)

label1=Label(frame1, text='Ad',font=('Helvetica 12 bold'),bg='#FF9999').pack(pady=2)
label1=Label(frame1, text='Soyad',font=('Helvetica 12 bold'),bg='#FF9999').pack(pady=2)
label1=Label(frame1, text='Yaş',font=('Helvetica 12 bold'),bg='#FF9999').pack(pady=2)
label1=Label(frame1, text='Doğum',font=('Helvetica 12 bold'),bg='#FF9999').pack(pady=2)
label1=Label(frame1, text='Cinsiyet',font=('Helvetica 12 bold'),bg='#FF9999').pack(pady=2)

label2=Label(frame2,text=':',font=('Helvetica 12 bold'),bg='#FF9999').pack(pady=2)
label2=Label(frame2,text=':',font=('Helvetica 12 bold'),bg='#FF9999').pack(pady=2)
label2=Label(frame2,text=':',font=('Helvetica 12 bold'),bg='#FF9999').pack(pady=2)
label2=Label(frame2,text=':',font=('Helvetica 12 bold'),bg='#FF9999').pack(pady=2)
label2=Label(frame2,text=':',font=('Helvetica 12 bold'),bg='#FF9999').pack(pady=2)

Entry(frame3,font=('Helvetica 12 bold')).pack(pady=2)  #ad
Entry(frame3,font=('Helvetica 12 bold')).pack(pady=2)  #soyad

Button(pencere,text='Kaydet',font=('Helvetica 12 bold'),bg='green',width=12).place(x=100 ,y=270)
Button(pencere,text='Temizle',font=('Helvetica 12 bold'),bg='red',width=12).place(x=270 ,y=270)
# photo= PhotoImage(file='person.png')
# resizedphoto=photo.subsample(4,4)
# Button(pencere,text='Yükle',font=('Helvetica 12 '),image=resizedphoto,compound=TOP).place(x=300,y=11)

Spinbox(frame3,from_=18,to=65,font=('Helvetica 12 bold'),width=19,justify=CENTER).pack(pady=2)

optionList=['Ocak','Şubat','Mart','Nisan','Mayıs','Haziran','Temmuz','Ağustos','Eylül','Ekim','Kasım','Aralık']
sval=StringVar(frame3)
sval.set(optionList[0])
optionm=OptionMenu(frame3,sval,*optionList)
optionm.config(font=('Helvetica 12 '),width=16,height=1)
optionm.pack(pady=2)

ivar=IntVar()
Radiobutton(frame3,text='Kadın',variable=ivar,value=1,font='Helvetica 12 ', bg='#FF9999').pack(side='left')
Radiobutton(frame3,text='Erkek',variable=ivar,value=2,font='Helvetica 12 ',bg='#FF9999').pack(side='left')

Checkbutton(frame4,text='Formu okudum, onaylıyorum.').pack(side='bottom')

cv=Canvas(frame5,bg='#FF9999',highlightthickness=10, highlightbackground='#FF9999')
cv.create_line(100,10 , 500,10)
cv.pack()



pencere.mainloop()