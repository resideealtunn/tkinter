#tablo oluşturma
import sqlite3 as sql           #db=database ,  veri tabanı
con=sql.connect("student.db")     #connection ; olusturdugumuz db ile program arasında bağ - student.db yoksa oluşturur varsa bağlantı kurar
#!DB Browser uygulaması! ile bir students veri tabanı oluştu, tablo oluşturacağız;
cur = con.cursor()              #imleci konumlandırdık
#execute("") kullanımı= tırnak içine -> CREATE TABLE tablo_ismi (col1 TEXT , col2 INT , col3 TEXT ) TEXT VS TİP BELİRTTİK
#execute("CREATE TABLE IF NOT EXISTS tablo_ismi ...") tablo yoksa oluştur, hata vermesin diye
cur. execute("CREATE TABLE IF NOT EXISTS grade (name TEXT, lesson TEXT , grade INT)")
#tabloya kayıt ekleme , ınsert;
# .execute("INSERT INTO tablo_ismi VALUES (value1,value2,value3)")
"""
cur.execute("INSERT INTO grade VALUES ('Reshide','AVP',102)")
cur.execute("INSERT INTO grade VALUES ('Fatma','fizik',90)")
cur.execute("INSERT INTO grade VALUES ('Mahmut','ingilizce',88)") #çalıştığı sürece hepsini listeye baştan yazar
con.commit()  #insert commit ile çalışır. yazılan komutları run ettirdik, execute tek başına yetersiz ,en sona bi tane yazılabilir yada aralara eklenebilir, db'e veri yüklüyor
"""
#dbden veri çekme , select;
# .execute("SELECT * FROM tablo_ismi ...")
# * tüm verileri çeker, * yerine çekilmek istenen verinin/lerin adı yazılabilir : SELECT name,grade FROM tablo_ismi
# örn; sadece matematik notlular çekilmek istenirse -> SELECT * FROM tablo_ismi WHERE şart_ifadesi (col1=value1)
cur.execute("SELECT * FROM grade")      #dbden veri çektik
data= cur.fetchall()                    #çekilen veriyi data değişkenine kaydettik, data değişkeninin türü listedir, bilgileri tuple tutar
#print(type(data))
#print(data)
# for i in data:
#     print(i)
cur.execute("SELECT * FROM grade WHERE lesson='AVP'")
veri=cur.fetchall()
#print(veri)
#veri güncelleme , update
# .execute("UPDATE tablo_ismi SET colx=valuex WHERE col1=value1) valx yeni değer
cur.execute("UPDATE grade SET lesson='matematik' WHERE lesson='ingilizce'")
con.commit()        #update de commitle çalışır
#tablodan veri silme , delete
#.execute("DELETE FROM tablo_ismi WHERE col1=val1")
#DELETE FROM tablo_ismi denilirse tüm satırları siler
cur.execute("DELETE FROM grade WHERE grade<60")
con.commit()        #veri tabanından da silindiği için commitle kullanılır

con.commit()
con.close()