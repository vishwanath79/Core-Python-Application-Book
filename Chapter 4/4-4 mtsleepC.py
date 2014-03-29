# 4-4 Using the threading module

import threading
from time import sleep,ctime
loops = [4,2]

def loop(nloop,nsec):
    print 'start loop',nloop,'at',ctime()
    sleep(nsec)
    print 'loop',nloop,'done at: ',ctime()
    
def main():
    print 'starting at:', ctime()
    threads=[]
    nloops = range(len(loops))
    print len(loops)
    print nloops
    for i in nloops:
        # Call loop()
        t=threading.Thread(target=loop,args=(i,loops[i]))
        threads.append(t)
        
    for i in nloops:
        # Let the threads go off to the races
        threads[i].start()
    
    for i in nloops:
        # Join will wait till each thread terminates or if a timeout occurs. Useful when you want to wait for thread completion.
        threads[i].join()
        
    print 'all done at: ',ctime()

    
main()