from multiprocessing import shared_memory

my_list = [10, 20, 30, 40, 50]

shma = shared_memory.SharedMemory(create=True, size=5)

shma.buf[:] = bytes(my_list)

print("Shared memory name:", shma.name)
print("Terminal 1 list:", list(shma.buf))

input("Press Enter to cleanup..")

shma.close()
shma.unlink()


"""         CPU
 ┌─────────────────────┐
 │ Core 0      Core 1  │
 │ Registers   Registers│
 │ L1 Cache    L1 Cache│
 │ L2 Cache    L2 Cache│
 │      L3 Cache       │
 └──────────┬──────────┘
            │
     Memory Controller
            │
 ┌──────────▼──────────┐
 │     System RAM      │
 │                     │
 │ Shared Memory       │
 │ [10, 20, 30, 40, 50]│
 └─────────────────────┘
       ▲           ▲
       │           │
   Process A   Process B

1. Linux creates a shared-memory object and maps it into Process A's virtual address space.
2. Physical RAM pages are generally allocated when accessed.
3. Process B attaches to the same object using its name.
4. Both processes can access the same physical RAM pages through their respective virtual addresses.
5. CPU caches may temporarily hold copies of the shared data for faster access.
Does each CPU core have its own copy?
CPU cores may cache the same shared-memory data in their private L1/L2 caches.
"""


