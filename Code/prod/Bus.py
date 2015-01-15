'''
    Created on Mar 30, 2014
    Last updated on Apr 6, 2014

    The class Bus represents one or more words communicated among subsystems.                

    @author: Andrew K. Marshall
    
    LOC: 23
'''
import CA04.prod.Command as command
import CA04.prod.Status as status
import CA04.prod.Data as data

from collections import deque

class Bus(object):

    '''
        Inits a new Bus
    '''
    def __init__(self):
        
        self.busQueue = deque([])
        
    '''
        Writes to the Bus. Checks to make sure it is a valid word.
        
        Returns the number of words on the bus.
    '''
    def writeBus(self, word=None):
          
        paramError = True
        
        if (isinstance(word, command.Command)):
            paramError = False
            
        elif (isinstance(word, status.Status) and paramError == True):
            paramError = False
            
        elif (isinstance(word, data.Data) and paramError == True):
            paramError = False
            
        elif (word == None and paramError == True):
            paramError = False
            
        if (paramError == True):
            raise ValueError("Bus.writeBus:  word must be a valid Command, Data, or Status word")
        
        self.busQueue.append(word)
        
        return self.busQueue.__len__()

    '''
        Returns the oldest Word on the Bus.
    '''
    def readBus(self):
        
        if (self.busQueue.__len__() == 0):
            raise ValueError("Bus.readBus:  Can not read an empty bus")
        
        return self.busQueue.popleft()
