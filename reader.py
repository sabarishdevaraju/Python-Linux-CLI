from multiprocessing import shared_memory

shmb = shared_memory.SharedMemory(name='psm_26479f21')

my_list = list(shmb.buf)


print("Terminal 2 list:", my_list)

shmb.buf[0] = 99

print("Updated shared list:", list(shmb.buf))

shmb.close()

"""TERMINAL 1 (Process A)
my_list = [10, 20, 30, 40, 50]
            |
            | bytes(my_list)
            v
     Shared Memory Buffer
     [10, 20, 30, 40, 50]
            ^
            |
            | list(shmb.buf)
            |
TERMINAL 2 (Process B)
my_list = [10, 20, 30, 40, 50]"""

#ls -lh /dev/shm