'''
    Created on Mar 30, 2014
    Last updated on Apr 6, 2014

    The class Data represents a data word transmitted to or received from the remote terminal.                

    @author: Andrew K. Marshall
    
    LOC: 20
'''

class Data(object):

    '''
        Inits a new Data.
    '''
    def __init__(self, payloadIn=None):
        
        if (payloadIn != None):
            # 0 <= (address must be) <= 65535
            if (payloadIn > 65535 or payloadIn < 0):
                raise(ValueError, "Data.__init__:  payload must be in the range of 0-65535")
            if (not isinstance(payloadIn, int)):
                raise ValueError("Data.__init__:  payload must be an integer")
        
        if (payloadIn == None):
            self.payload = 0
        else:
            self.payload = payloadIn
            
        
    '''
         Sets the payload.  Must be between 0 - 65535
    '''
    def setContent(self, payloadIn):
        # 0 <= (address must be) <= 65535
        if (payloadIn > 65535 or payloadIn < 0):
            raise ValueError("Data.setContent:  payload must be in the range of 0-65535")
        if (not isinstance(payloadIn, int)):
            raise ValueError("Data.setContent:  payload must be an integer")
        
        self.payload = payloadIn
        
        return payloadIn
    
    '''
         Gets the payload.
    '''
    def getContent(self):
        return self.payload
