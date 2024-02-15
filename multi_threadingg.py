import threading
import time

def subfunction1():
    time.sleep(2)
    print('sub1: start')
    time.sleep(2)
    print('sub1: finito')
    time.sleep(2)

def subfunction2(val1,val2):
    time.sleep(2)
    print('sub2: start'+', val1:'+val1+', val2:'+val2)
    time.sleep(2)
    print('sub2: finito')
    time.sleep(2)

def mainfunction():
    print('main: aktif')
    t1=threading.Thread(target=subfunction1)
    t2=threading.Thread(target=subfunction2,args=('reşide','altun'))
    t1.start()
    t2.start()
    t1.join()
    #t2.join()
    print('main: inaktif')
mainfunction()