import threading
import time

answer = 0

def job(inputValue):
    print("inputValue is " + str(inputValue))
    global answer
    answer = inputValue + 1
    print("thread answer is " + str(answer))
    time.sleep(2)
    print("end job")
    
a = 2   
firstThread = threading.Thread(target = job, args=(a,))
firstThread.start()
print("please wait for process")
firstThread.join()
print("answer is " + str(answer))



