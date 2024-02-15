from tkinter import *
#bg,height,width,cursor,highlighthickness, highlightbackground,
#line,oval,arc,polygon,image
window= Tk()
window.geometry('400x500')

cv = Canvas(window,bg='green',width=300,height=400)
#cv.create_line(0,0 , 100,100 , 200,100 , 200,300,dash=(13,13)) #çizgi çizmek - (x1,y1, x2,y2, x3,y3..) dash: kesikli çizgi
#cv.create_oval(10,10, 150,150, fill='blue', outline='red',width=10      #oval,çember çizmek - width: çember kenar kalınlığı - outline: kenar rengi
#saylar belirlenip değişkene atanıp create içine değişken yazılabilir;
coor=10,10,150,150
#cv.create_arc(coor,start=20,extent=190,fill='pink')    #açı çizmek
#arc ve ovalde aslında bir dikdörtgen oluşturup içine çiziyor
#cv.create_polygon(0,75, 75,0, 150,75, 75,150 , fill='lightblue')        #esnek şekiller çizmemizi sağlar
photo=PhotoImage(file='vangogh.png')
photoresized=photo.subsample(6,6)
cv.create_image(150,150, image=photoresized) #150,150(başlangıç noktası)



cv.pack()








window.mainloop()