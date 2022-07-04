import threading
import time

printerLock = threading.Lock()
screenLock = threading.Lock()
def process1():
    printerLock.acquire() 
    print("process1 get print lock")
    time.sleep(1)
    screenLock.acquire()
    print("process1 get screen lock")
    time.sleep(1)
    print("process1 finish")
    printerLock.release()
    screenLock.release()
    
def process2():
    screenLock.acquire()
    print("process2 get screen lock")
    printerLock.acquire() 
    print("process2 get print lock")
    time.sleep(1)
    print("process2 finish print lock")
    screenLock.release()
    printerLock.release()
    
firstThread = threading.Thread(target = process1)
secondThread = threading.Thread(target = process2)
firstThread.start()
secondThread.start()
firstThread.join()
secondThread.join()
print("end all")
