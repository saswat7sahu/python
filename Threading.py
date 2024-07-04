#thread:A thread is the smallest unit of a process that can be scheduled and executed by the operating system
#Threads are useful in scenarios where you need to perform multiple operations at once, especially when one or more of those operations might block the main execution flow (like I/O operations)
import threading
def run():
    for i in range(20):
        print(i)
def run2():
    for i in range(30):
        print(i)
def run3():
    for i in range(5):
        print(i)
th1=threading.Thread(target=run)
th2=threading.Thread(target=run2)
th1.start()
th2.start()
#stop After the two thread stopped then the 3rd thread will start by join()
th1.join()
th2.join()
th3=threading.Thread(target=run3)
th3.start()