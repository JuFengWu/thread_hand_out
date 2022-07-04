import threading
import time


def job(threadIndex,testString):
    firstString = "in thread index" + str(threadIndex)
    testString.append(firstString)
    secondString = "ready finish thread index" + str(threadIndex)
    testString.append(secondString)
