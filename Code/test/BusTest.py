'''
    Created on Apr 2, 2014
    Last updated on Apr 6, 2014

    This is a test file used to test the Bus Class

    @author: Andrew K. Marshall
'''
import unittest

import prod.Bus as bus
import prod.Command as command
import prod.Status as status
import prod.Data as data
import prod.RemoteTerminal as remoteTerminal


class busTest(unittest.TestCase):

# Bus
# methods: instantiate, writeBus, readBus

    ''' 
        Called before every method.  Creates a valid word instance of a Command, Data, and Status.
    '''
    
    def setUp(self):
        self.myCommandWord = command.Command(1)
        self.myStatusWord = status.Status(15)
        self.myDataWord = data.Data(20)

    '''
        Test: Instantiate Bus()
    '''
    def test_001_001_InstantiateBus(self):
        myBus = bus.Bus()
        
        theResult1 = True
        theResult2 = 0
        
        self.assertEquals(theResult1, isinstance(myBus, bus.Bus))
        self.assertEquals(theResult2, myBus.busQueue.__len__())
        
# writeBus

    '''
        Test: Add a valid Command word to the bus
    '''
    def test_002_001_writeBus(self):
        myBus = bus.Bus()
        
        theResult1 = 1
        theResult2 = True
        theResult3 = 0
        
        self.assertEquals(theResult1, myBus.writeBus(self.myCommandWord))
        self.assertEquals(theResult1, myBus.busQueue.__len__())
        self.assertEquals(theResult2, isinstance(myBus.busQueue.popleft(), command.Command))
        self.assertEquals(theResult3, myBus.busQueue.__len__())
        
    '''
        Test: Add a valid Status word to the bus
    '''
    def test_002_002_writeBus(self):
        myBus = bus.Bus()
        
        theResult1 = 1
        theResult2 = True
        theResult3 = 0
        
        self.assertEquals(theResult1, myBus.writeBus(self.myStatusWord))
        self.assertEquals(theResult1, myBus.busQueue.__len__())
        self.assertEquals(theResult2, isinstance(myBus.busQueue.popleft(), status.Status))
        self.assertEquals(theResult3, myBus.busQueue.__len__())
        
    '''
        Test: Add a valid Data word to the bus
    '''
    def test_002_003_writeBus(self):
        myBus = bus.Bus()
        
        theResult1 = 1
        theResult2 = True
        theResult3 = 0
        
        self.assertEquals(theResult1, myBus.writeBus(self.myDataWord))
        self.assertEquals(theResult1, myBus.busQueue.__len__())
        self.assertEquals(theResult2, isinstance(myBus.busQueue.popleft(), data.Data))
        self.assertEquals(theResult3, myBus.busQueue.__len__())
        
    '''
        Test: Add a valid Status word, then Command word, then Status word, then Data word
    '''
    def test_002_004_writeBus(self):
        myBus = bus.Bus()
        
        self.assertEquals(1, myBus.writeBus(self.myStatusWord))
        self.assertEquals(1, myBus.busQueue.__len__())
        self.assertEquals(2, myBus.writeBus(self.myCommandWord))
        self.assertEquals(2, myBus.busQueue.__len__())
        self.assertEquals(3, myBus.writeBus(self.myStatusWord))
        self.assertEquals(3, myBus.busQueue.__len__())
        self.assertEquals(4, myBus.writeBus(self.myDataWord))
        self.assertEquals(4, myBus.busQueue.__len__())        
        
        self.assertEquals(True, isinstance(myBus.busQueue.popleft(), status.Status))
        self.assertEquals(3, myBus.busQueue.__len__())
        self.assertEquals(True, isinstance(myBus.busQueue.popleft(), command.Command))
        self.assertEquals(2, myBus.busQueue.__len__())
        self.assertEquals(True, isinstance(myBus.busQueue.popleft(), status.Status))
        self.assertEquals(1, myBus.busQueue.__len__())
        self.assertEquals(True, isinstance(myBus.busQueue.popleft(), data.Data))
        self.assertEquals(0, myBus.busQueue.__len__())
        
    '''
        Test: Bus.writeBus('a')
    '''
    def test_002_901_writeBus(self):
        myBus = bus.Bus()
        
        self.assertRaises(ValueError, myBus.writeBus, 'a')
        
    '''
        Test: Bus.writeBus(5)
    '''
    def test_002_902_writeBus(self):
        myBus = bus.Bus()
        
        self.assertRaises(ValueError, myBus.writeBus, 5)
        
    '''
        Test: Bus.writeBus(RemoteTerminal)
    '''
    def test_002_903_writeBus(self):
        myBus = bus.Bus()
        
        myRemTerm = remoteTerminal.RemoteTerminal(1)
        
        self.assertRaises(ValueError, myBus.writeBus, myRemTerm)
        
# Read Bus


    '''
        Test: Add a valid Status word to the bus. Call readBus()
    '''
    def test_003_001_readBus(self):
        myBus = bus.Bus()
        
        myBus.writeBus(self.myStatusWord)
        
        theResult1 = True
        
        self.assertEquals(theResult1, isinstance(myBus.readBus(), status.Status))
        self.assertEquals(0, myBus.busQueue.__len__())
        
    '''
        Test: Add a valid Command word to the bus. Call readBus()
    '''
    def test_003_002_readBus(self):
        myBus = bus.Bus()
        
        myBus.writeBus(self.myCommandWord)
        
        theResult1 = True
        
        self.assertEquals(theResult1, isinstance(myBus.readBus(), command.Command))
        self.assertEquals(0, myBus.busQueue.__len__())
        
    '''
        Test: Add a valid Data word to the bus. Call readBus()
    '''
    def test_003_003_readBus(self):
        myBus = bus.Bus()
        
        myBus.writeBus(self.myDataWord)
        
        theResult1 = True
        
        self.assertEquals(theResult1, isinstance(myBus.readBus(), data.Data))
        self.assertEquals(0, myBus.busQueue.__len__())
        
    '''
        Test: Add a valid Status word, then Command word, then Status word, then Data word. Then call readBus() until empty
    '''
    def test_003_004_readBus(self):
        myBus = bus.Bus()
        
        myBus.writeBus(self.myStatusWord)
        myBus.writeBus(self.myCommandWord)
        myBus.writeBus(self.myStatusWord)
        myBus.writeBus(self.myDataWord)
        
        theResult1 = True
        
        self.assertEquals(theResult1, isinstance(myBus.readBus(), status.Status))
        self.assertEquals(3, myBus.busQueue.__len__())
        self.assertEquals(theResult1, isinstance(myBus.readBus(), command.Command))
        self.assertEquals(2, myBus.busQueue.__len__())
        self.assertEquals(theResult1, isinstance(myBus.readBus(), status.Status))
        self.assertEquals(1, myBus.busQueue.__len__())
        self.assertEquals(theResult1, isinstance(myBus.readBus(), data.Data))
        self.assertEquals(0, myBus.busQueue.__len__())
        
    '''
        Test: Call readBus() on an empty bus
    '''
    def test_003_901_readBus(self):
        myBus = bus.Bus()
        
        self.assertRaises(ValueError, myBus.readBus)
        
        
        
        
        
        
        
        
        
        
        
        
