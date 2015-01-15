'''
    Created on Mar 30, 2014
    Last updated on Apr 6, 2014

    The class Status represents information regarding the current state of a remote terminal.

    @author: Andrew K. Marshall
    
    LOC: 40
'''

class Status(object):
    
    '''
        Inits a new Status.
    '''
    def __init__(self, addressIn):
        
        # 1 <= (address must be) <= 30
        if (addressIn > 30 or addressIn < 1):
            raise ValueError("Status.__init__:  address must be in the range of 1-30")
        if (not isinstance(addressIn, int)):
            raise ValueError("Status.__init__:  address must be an integer")
        
        self.address = addressIn
        self.serviceRequestFlag = False
        self.messageErrorFlag = False
        self.busyFlag = False        
    
    '''
        Returns the Remote Terminal's Address
    '''    
    def getTerminalAddress(self):
        
        return self.address
    
    '''
        Sets the Service Request Flag.
        
        Returns True if the flag was already set.
    '''
    def setServiceRequest(self):
        
        if (self.serviceRequestFlag == True):
            temp = True
        else:
            temp = False
        
        self.serviceRequestFlag = True
        return temp
    
    '''
        Returns isServiceRequest
    '''
    def isServiceRequested(self):
        return self.serviceRequestFlag

    '''
        Sets the Message Error Flag.
        
        Returns True if the flag was already set.
    '''
    def setMessageError(self):
        
        if (self.messageErrorFlag == True):
            temp = True
        else:
            temp = False
        
        self.messageErrorFlag = True
        return temp
    
    '''
        Returns isServiceRequest
    '''
    def isMessageError(self):
        return self.messageErrorFlag
    
    '''
        Sets the Busy Flag.
        
        Returns True if the flag was already set.
    '''
    def setBusy(self):
        
        if (self.busyFlag == True):
            temp = True
        else:
            temp = False
        
        self.busyFlag = True
        return temp
    
    '''
        Returns isServiceRequest
    '''
    def isBusy(self):
        return self.busyFlag
    
    
