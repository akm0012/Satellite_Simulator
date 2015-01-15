'''
Created on Apr 2, 2014

@author: Andrew
'''

import Queue

if __name__ == '__main__':
    
    myQueue = Queue.Queue()
    
    myQueue.put(5)
    
    myQueue.put(10)
    
    myQueue.put(15)
    
    size = myQueue.qsize()
    
    print size
    
    print myQueue.get()
    
    size = myQueue.qsize()
    
    print size
    
    
    