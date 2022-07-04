import threading
import time

def atm(atmIndex,getMoney):
    global accountMoney
    atmMoney = accountMoney
    print("atm"+str(atmIndex) +" is connect with server")
    time.sleep(2)
    print("machine"+str(atmIndex) +" is running")
    time.sleep(2)
    accountMoney = atmMoney - getMoney
    print("atm"+str(atmIndex) +" is re-new money to server")
    time.sleep(2)
    print("money get from atm is " + str(getMoney))

global accountMoney
accountMoney = 300
print("initial money in bank is " + str(accountMoney))
firstThread = threading.Thread(target = atm, args=(1,100,))
secondThread = threading.Thread(target = atm, args=(2,100,))
print("get money from first atm")
firstThread.start()
print("get money from second atm")
secondThread.start()
firstThread.join()
secondThread.join()
print("get all money, money in bank is " + str(accountMoney))
