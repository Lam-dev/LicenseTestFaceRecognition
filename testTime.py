#!/usr/bin/python
import time

def procedure():
   time.sleep(2.5)

# measure process time
t0 = time.clock()
procedure()
print (time.clock(), "seconds process time")
# time.clock_settime
# measure wall time
t0 = time.time()
procedure()
print (time.time() - t0, "seconds wall time")