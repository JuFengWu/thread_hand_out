import  threading
import time 
import datetime

def process1():
    print("start process")
    global isOK
    isOK = False 
    time.sleep(5.5)
    print("finish process")
    isOK = True


isOK = False
firstThread = threading.Thread(target = process1)
firstThread.start()
while(not isOK):
    now = datetime.datetime.now()
    print("not ok, current time is " + str(now))
    time.sleep(1)
now = datetime.datetime.now()  
print("all ok , current time is "+ str(now))
