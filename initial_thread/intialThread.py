import threading
import time

def job():
    for i in range(5):
        print("in thread:", i)
        time.sleep(0.5)
    print("end job")
firstThread = threading.Thread(target = job)

firstThread.start()

for i in range(3):
  print("int mian :", i)
  time.sleep(0.5)

firstThread.join()

print("all finish")



