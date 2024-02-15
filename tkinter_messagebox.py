from tkinter import *
from tkinter import messagebox

#Information Messages(bilgi)
#showinfo()

#Warning Messages(uyarı)
#showwarning
#showerror

#Question Messages
#askquestion()
#askokcancel()
#askretrycancel()
#askyesno()
#askyesnocancel()


window=Tk()
window.geometry('400x300')


def clicked_button():
    #messagebox.showinfo('showinfo','information aga be careful yani')       #2pm, 1.title 2.uyarı mesajı
    #messagebox.showwarning('Show Warning','warning uyarı demektir')
    # response=messagebox.showerror('Show error','404 file not found asko')
    # print(response)         #tıklanılan tuşu terminale bastırır
    # response=messagebox.askquestion('Ask Question','are you hungry?')
    # print(response)
    # response=messagebox.askokcancel('Ask Ok Cancel','Devam etmek istiyor musun?')
    # print(response)
    # response=messagebox.askretrycancel('Ask reTry Cancel','Exten next olur mu?')
    # print(response)
    # response=messagebox.askyesno('Ask Yes No','yes or no?')
    # print(response)
    response=messagebox.askyesnocancel('Ask Yes No Cancel','seç aga birini')
    print(response)
Button(window,text='Click me!',command=clicked_button).pack(

)

window.mainloop()