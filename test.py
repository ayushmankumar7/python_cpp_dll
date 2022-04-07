import time 
import ctypes 

x = 1000

# Read DLL file using ctypes
dll = ctypes.CDLL("./bin/program.dll")

# Calling our print_loop function
t = time.time()
dll.print_loop(x)    
te = time.time()

t1 = time.time()
for i in range(x):
    print(i)


print("Time taken by DLL:", te-t)
print("Time taken by Native Python:", time.time() - t1)