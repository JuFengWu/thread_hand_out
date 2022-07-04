import threading
import time

printerLock = threading.Lock()
screenLock = threading.Lock()
def process1():
    getPrintLock = printerLock.acquire(timeout = 1) 
    if getPrintLock :
        print("process1 get print lock")
        time.sleep(1)
    else:
        print("process1 not get print lock")
    getScreenLock = screenLock.acquire(timeout = 1)
    if getScreenLock:
        print("process1 get screen lock")
        time.sleep(1)
    else:
        print("process1 not get screen lock")
    print("process1 finish")
    if getPrintLock:
        printerLock.release()
    if getScreenLock:
        screenLock.release()
    
def process2():
    getScreenLock = screenLock.acquire(timeout = 1)
    if getScreenLock:
        print("process2 get screen lock")
        time.sleep(1)
    else:
        print("process2 not get screen lock")
    getPrintLock = printerLock.acquire(timeout = 1) 
    if getPrintLock:
        print("process2 get print lock")
        time.sleep(1)
    else:
        print("process2 not get print lock")
    print("process2 finish print lock")
    if getScreenLock:
        screenLock.release()
    if getPrintLock:
        printerLock.release()
    
firstThread = threading.Thread(target = process1)
secondThread = threading.Thread(target = process2)
firstThread.start()
secondThread.start()
firstThread.join()
secondThread.join()
print("end all")
