from multiprocessing import shared_memory   
from mediaquery.lib.Argument import Argument
import sys

args = Argument(sys.argv)

if(not args.hasOptions(['--shm','--pname'])):
    print('Usage: {} --shm=NAME --pname=[master|slave]'.format(sys.argv[0]))
    exit(1)

if(args.getOptionValue('--pname') == 'master'):
    shm = shared_memory.SharedMemory(name=args.getOptionValue('--shm'), create=True, size=1024)
else:
    shm = shared_memory.SharedMemory(name=args.getOptionValue('--shm'))

def writeShmString(shm, data):
    buf = shm.buf
    buf[:len(data)] = bytearray(data, 'utf-8')

def readShmString(shm):
    buf = shm.buf
    return str(buf, 'utf-8').rstrip('\x00')


try:
    while True:
        choice = input('1: Read SHM; 2: Write SHM; 3: Close SHM; Choose > ')
        if choice == '1':
            print(readShmString(shm))
        elif choice == '2':
            val = input('Enter a string to write to SHM > ')
            writeShmString(shm, val)
        elif choice == '3':
            shm.close()
            shm.unlink()
            break
except KeyboardInterrupt:
    shm.close()
    shm.unlink()
    print("\nProgram terminated by user.")

# 
# 
# python3 sharedmem.py --shm=snamem2 --pname=master
# 
