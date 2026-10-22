
import threading
import time
import os

def task(number):
    print(f"Thread {number}, PID: {os.getpid()}")
    time.sleep(2)
    print(f"Thread {number} finished")

threads = []

for i in range(3):
    t = threading.Thread(target=task, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All threads completed")
