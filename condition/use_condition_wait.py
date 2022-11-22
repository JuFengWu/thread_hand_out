import  threading
import time 
import datetime



def process1(cndition):
    print('process1 start.')
    time.sleep(0.5)
    cndition.acquire()
    print('process1 acquires lock.')
    print("start process")
    time.sleep(2)
    
    print("finish process")
    cndition.notify()
    cndition.release()
    
def process2(cndition):
    
    print('process2 start.')
    cndition.acquire()
    print('process2 acquires lock.')
    now = datetime.datetime.now()
    print("start, current time is " + str(now))
    cndition.wait()
    now = datetime.datetime.now()  
    print("all ok , current time is "+ str(now))

cndition = threading.Condition()

firstThread = threading.Thread(target = process1, args=(cndition,))
firstThread.start()
secondThread = threading.Thread(target = process2, args=(cndition,))
secondThread.start()

