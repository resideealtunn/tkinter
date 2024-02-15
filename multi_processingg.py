from multiprocessing import Process
import time

def subfunction1():
    time.sleep(2)
    print('sub1: start')
    time.sleep(2)
    print('sub1: finito')
    time.sleep(2)

def subfunction2():
    time.sleep(2)
    print('sub2: start')
    time.sleep(2)
    print('sub2: finito')
    time.sleep(2)

def mainfunction():
    print('main: aktif')
    p1=Process(target=subfunction1)
    p2=Process(target=subfunction2)
    p1.start()
    p2.start()
    p1.join()       #main bloğu tüm işlemler bitmeden kapanmasın diye join kullanılır
    p2.join()
    print('main: inaktif')

if __name__=='__main__':
    mainfunction()

"""
#kod multiprocessing'siz bu şekilde
import time

def subfunction1():
    time.sleep(2)
    print('sub1: start')
    time.sleep(2)
    print('sub1: finito')
    time.sleep(2)

def subfunction2():
    time.sleep(2)
    print('sub2: start')
    time.sleep(2)
    print('sub2: finito')
    time.sleep(2)

def mainfunction():
    print('main: aktif')
    subfunction1()
    subfunction2()
    print('main: inaktif')
"""