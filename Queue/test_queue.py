import threading
import time
import queue

def add_1_print(q):
  global isRun
  while isRun:
    if(not q.empty()):
        value = q.get()
        value = value +1
        print("value is " + str(value))
    time.sleep(1)
  print("end thread")

isRun = True
q = queue.Queue()
thread = threading.Thread(target = add_1_print, args=(q ,))
thread.start()
q.put(1)
q.put(2)
q.put(3)
time.sleep(5)
isRun = False
thread.join()
print("end all")
