from tkinter import *       # * tkinterin tüm fonksiyonlarını kullanacağız demek
window=Tk()                 #mainloop()suz arayüz oluşturmaz. kodları bu iki satırın arasına yazacağız
#başlık verme , title
window.title('Tkinter Giriş Videosu')
#backgorund rengi değiştirme
window.configure(background='yellow')   #background yerine bg yazılabilir, html renk kodları da kullanılabilir
#window.configure(background='#658958')
#size değiştirme
window.geometry('300x300+750+200') #1.en 2. boy 3. soldan bırakılan uzaklık 4. yukarıdan bırakılan uzaklık
#icon değiştirme
window.iconbitmap('stopwatch.ico')  #ico uzantılı olmalı
#transparanlık
window.attributes('-alpha',0.9)
#pencereyi hep en önde tutmak
window.attributes('-topmost',1)
#ekran boyutunu sabitleme
window.resizable(height=True, width=True) #kapatmak istemediğine True, istediğine False yazarsın
#max ve min boyutlar belirleme
window.minsize(200, 200)
window.maxsize(600, 600)
"""
#tüm ekran fullscreen yapma
window.attributes('-fullscreen',True)
window.bind("<Escape>", lambda event: window.attributes('-fullscreen',False)) #esc ye basıldığında ekranı kapat
window.bind("<F11>",lambda event:window.attributes('-fullscreen',not window.attributes('-fullscreen')))  #f11e basıldığında ekran büyükse küçült küçükse büyüt
                                                                 #o an ekran nasılsa DEĞİLine çevir -> not
"""





window.mainloop()
