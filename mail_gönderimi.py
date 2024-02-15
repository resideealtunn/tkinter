import smtplib

title='Subject:Deneme Başlığı'
message='Deneme mail içeriği'
content=title+ '\n' + message      #İÇERİK
#content='içerik' şeklinde de yapılabilir, başlık vermek için böyle yaptık
sender='resideealtunn@gmail.com'    #GÖNDEREN
password='mfralt123R'               #şifre
to='residealtun22@gmail.com'        #gönderilen hesap

server=smtplib.SMTP("smtp.gmail.com",587)
server.ehlo()
server.starttls()
server.login(sender,password)
server.sendmail(sender,to,content.encode('utf-8'))
server.close()
#mailin bu halinde hata alınmasının sebebi gmail uygulamasında 3.taraftan gelen maillere hsabın kapalı olmasıdır