import os
import time

r, w = os.pipe()
s ="sam01"

if(os.fork() == 0): #running process will be cloned and create new child process from existing parent process
    print(f'Child Process ID: { str(os.getpid())}')
    while True:
        time.sleep(0.1)
        os.write(w, bytes(input('Send data to prevent from PID: {}:'.format(os.getpid())), 'utf-8'))
else:
    print(f'Parent Process ID: {str(os.getpid())}')
    while True:
        print("Data received to PID: {}: ".format(os.getpid())+str(os.read(r, 100), 'utf-8'))