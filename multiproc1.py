
import multiprocessing
import time
import os

def task(number):
    print(f"Process {number}, PID: {os.getpid()}")
    time.sleep(2)
    print(f"Process {number} finished")

if __name__ == "__main__":
    processes = []

    for i in range(3):
        p = multiprocessing.Process(target=task, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("All processes completed")
