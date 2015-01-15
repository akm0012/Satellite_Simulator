'''
    Created on Mar 30, 2014
    Last updated on Apr 6, 2014

    This is a test file used to test the Class Status

    @author: Andrew K. Marshall
'''
import unittest

import CA04.prod.Status as status


class statusTest(unittest.TestCase):

# Status
# methods: instantiate, getTerminalAddress, setServiceRequest, isServiceRequested, setMessageError
#          isMessageError, setBusy, isBusy  

# Constructor
    '''
        Test: Instantiate Status(1)
    '''
    def test100_010_InstantiateStatus(self):
        myStatus = status.Status(1)
        
        theResult1 = True
        theResult2 = 1
        theResult3 = False
        theResult4 = False
        theResult5 = False
        
        self.assertEquals(theResult1, isinstance(myStatus, status.Status))
        self.assertEquals(theResult2, myStatus.address)
        self.assertEquals(theResult3, myStatus.serviceRequestFlag)
        self.assertEquals(theResult4, myStatus.messageErrorFlag)
        self.assertEquals(theResult5, myStatus.busyFlag)
    # END: test100_010_InstantiateStatus
    
    '''
        Test: Instantiate Status(15)
    '''
    def test100_020_InstantiateStatus(self):
        myStatus = status.Status(15)
        
        theResult1 = True
        theResult2 = 15
        theResult3 = False
        theResult4 = False
        theResult5 = False
        
        self.assertEquals(theResult1, isinstance(myStatus, status.Status))
        self.assertEquals(theResult2, myStatus.address)
        self.assertEquals(theResult3, myStatus.serviceRequestFlag)
        self.assertEquals(theResult4, myStatus.messageErrorFlag)
        self.assertEquals(theResult5, myStatus.busyFlag)
    # END: test100_020_InstantiateStatus 
    
    '''
        Test: Instantiate Status(30)
    '''
    def test100_030_InstantiateStatus(self):
        myStatus = status.Status(30)
        
        theResult1 = True
        theResult2 = 30
        theResult3 = False
        theResult4 = False
        theResult5 = False
        
        self.assertEquals(theResult1, isinstance(myStatus, status.Status))
        self.assertEquals(theResult2, myStatus.address)
        self.assertEquals(theResult3, myStatus.serviceRequestFlag)
        self.assertEquals(theResult4, myStatus.messageErrorFlag)
        self.assertEquals(theResult5, myStatus.busyFlag)
    # END: test100_030_InstantiateStatus
    
    '''
        Test: Instantiate Status(0)
    '''
    def test100_910_InstantiateStatus(self):
        self.assertRaises(ValueError, status.Status, 0)
    # END: test100_910_InstantiateStatus
    
    '''
        Test: Instantiate Status(31)
    '''
    def test100_920_InstantiateStatus(self):
        self.assertRaises(ValueError, status.Status, 31)
    # END: test100_920_InstantiateStatus
    
    '''
        Test: Instantiate Status('a')
    '''
    def test100_930_InstantiateStatus(self):
        self.assertRaises(ValueError, status.Status, 'a')
    # END: test100_930_InstantiateStatus
    
    '''
        Test: Instantiate Status('%')
    '''
    def test100_940_InstantiateStatus(self):
        self.assertRaises(ValueError, status.Status, '%')
    # END: test100_940_InstantiateStatus
    
# getTerminalAddress
    
    '''
        Test: Instantiate Status(1). Call getTerminalAddress()
    '''
    def test200_010_getTerminalAddress(self):
        myStatus = status.Status(1)
        
        theResult1 = 1
        
        self.assertEquals(theResult1, myStatus.getTerminalAddress())
    # END: test200_010_getTerminalAddress

    '''
        Test: Instantiate Status(15). Call getTerminalAddress()
    '''
    def test200_020_getTerminalAddress(self):
        myStatus = status.Status(15)
        
        theResult1 = 15
        
        self.assertEquals(theResult1, myStatus.getTerminalAddress())
    # END: test200_020_getTerminalAddress

    '''
        Test: Instantiate Status(30). Call getTerminalAddress()
    '''
    def test200_030_getTerminalAddress(self):
        myStatus = status.Status(30)
        
        theResult1 = 30
        
        self.assertEquals(theResult1, myStatus.getTerminalAddress())
    # END: test200_030_getTerminalAddress
    
# setServiceRequest

    '''
        Test: Instantiate Status(1). Call setServiceRequest()
    '''
    def test300_010_setServiceRequest(self):
        myStatus = status.Status(1)
        
        theResult1 = False
        theResult2 = True
                
        self.assertEquals(theResult1, myStatus.setServiceRequest())
        self.assertEquals(theResult2, myStatus.serviceRequestFlag) 
    # END: test300_010_setServiceRequest

    '''
        Test: Instantiate Status(1). Call setServiceRequest() twice
    '''
    def test300_020_setServiceRequest(self):
        myStatus = status.Status(1)
        
        theResult1 = True
        theResult2 = True
        
        myStatus.setServiceRequest()
        
        self.assertEquals(theResult1, myStatus.setServiceRequest())
        self.assertEquals(theResult2, myStatus.serviceRequestFlag) 
    # END: test300_010_setServiceRequest

# isServiceRequested

    '''
        Test: Instantiate Status(1). Call setServiceRequest(). Call isServiceRequested()
    '''
    def test400_010_isServiceRequest(self):
        myStatus = status.Status(1)
        
        theResult1 = True
        theResult2 = True
        
        myStatus.setServiceRequest()
                
        self.assertEquals(theResult1, myStatus.isServiceRequested())
        self.assertEquals(theResult2, myStatus.serviceRequestFlag) 
    # END: test400_010_isServiceRequest
    
    '''
        Test: Instantiate Status(1). Call isServiceRequested()
    '''
    def test400_020_isServiceRequest(self):
        myStatus = status.Status(1)
        
        theResult1 = False
        theResult2 = False
                        
        self.assertEquals(theResult1, myStatus.isServiceRequested())
        self.assertEquals(theResult2, myStatus.serviceRequestFlag) 
    # END: test400_020_isServiceRequest
    
# setMessageError
    
    '''
        Test: Instantiate Status(1). Call setMessageError()
    '''
    def test500_010_setMessageError(self):
        myStatus = status.Status(1)
        
        theResult1 = False
        theResult2 = True
                        
        self.assertEquals(theResult1, myStatus.setMessageError())
        self.assertEquals(theResult2, myStatus.messageErrorFlag) 
    # END: test500_010_setMessageError

    '''
        Test: Instantiate Status(1). Call setMessageError() twice
    '''
    def test500_020_setMessageError(self):
        myStatus = status.Status(1)
        
        theResult1 = True
        theResult2 = True
        
        myStatus.setMessageError()
                        
        self.assertEquals(theResult1, myStatus.setMessageError())
        self.assertEquals(theResult2, myStatus.messageErrorFlag) 
    # END: test500_020_setMessageError

# isMessageError

    '''
        Test: Instantiate Status(1). Call setMessageError(). Call isMessageError()
    '''
    def test500_010_isMessageError(self):
        myStatus = status.Status(1)
        
        theResult1 = True
        theResult2 = True
        
        myStatus.setMessageError()
                
        self.assertEquals(theResult1, myStatus.isMessageError())
        self.assertEquals(theResult2, myStatus.messageErrorFlag) 
    # END: test500_010_isMessageError
    
    '''
        Test: Instantiate Status(1). Call isMessageError()
    '''
    def test500_020_isMessageError(self):
        myStatus = status.Status(1)
        
        theResult1 = False
        theResult2 = False
                        
        self.assertEquals(theResult1, myStatus.isMessageError())
        self.assertEquals(theResult2, myStatus.messageErrorFlag) 
    # END: test500_020_isMessageError
    
# setBusy

    '''
        Test: Instantiate Status(1). Call setBusy()
    '''
    def test600_010_setBusy(self):
        myStatus = status.Status(1)
        
        theResult1 = False
        theResult2 = True
                        
        self.assertEquals(theResult1, myStatus.setBusy())
        self.assertEquals(theResult2, myStatus.busyFlag) 
    # END: test500_010_setMessageError

    '''
        Test: Instantiate Status(1). Call setBusy() twice
    '''
    def test600_020_setBusy(self):
        myStatus = status.Status(1)
        
        theResult1 = True
        theResult2 = True
        
        myStatus.setBusy()
                        
        self.assertEquals(theResult1, myStatus.setBusy())
        self.assertEquals(theResult2, myStatus.busyFlag) 
    # END: test500_020_setMessageError

# isBusy

    '''
        Test: Instantiate Status(1). Call setBusy(). Call isBusy()
    '''
    def test700_010_isBusy(self):
        myStatus = status.Status(1)
        
        theResult1 = True
        theResult2 = True
        
        myStatus.setBusy()
                
        self.assertEquals(theResult1, myStatus.isBusy())
        self.assertEquals(theResult2, myStatus.busyFlag) 
    # END: test700_010_isBusy
    
    '''
        Test: Instantiate Status(1). Call isBusy()
    '''
    def test700_020_isBusy(self):
        myStatus = status.Status(1)
        
        theResult1 = False
        theResult2 = False
                        
        self.assertEquals(theResult1, myStatus.isBusy())
        self.assertEquals(theResult2, myStatus.busyFlag) 
    # END: test700_020_isBusy






