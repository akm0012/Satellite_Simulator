'''
    Created on Apr 19, 2014
    Last updated on Apr 19, 2014

    This is a test file used to test the BusController Class

    @author: Andrew K. Marshall
'''
import unittest

import CA05.prod.BusController as BusController
import CA04.prod.RemoteTerminal as RemoteTerminal
import CA05.prod.Satellite as Satellite



class BusControllerTest(unittest.TestCase):
    
# BusController
# methods: instantiate, setPollFrame(rtList), poll()


# Constructor
    
    '''
        Test: Instantiate BusController()
    '''
    def test_001_001_InstantiateBusController(self):
        myBusController = BusController.BusController()
        
        self.assertTrue(isinstance(myBusController, BusController.BusController))
        self.assertEquals(myBusController.pollFrame, [])

# setPollFrame

    '''
        Test: Call setPollFrame(0)
    '''
    def test_002_901_setPollFrame(self):
        myBC = BusController.BusController()
        
        self.assertRaises(ValueError, myBC.setPollFrame, 0)
        
        try:
            myBC.setPollFrame(0)
        except ValueError as myException:
            self.assertTrue(myException.args[0].startswith("BusController.setPollFrame:  "))
            
    '''
        Test: Call setPollFrame(15)
    '''
    def test_002_902_setPollFrame(self):
        myBC = BusController.BusController()
        
        self.assertRaises(ValueError, myBC.setPollFrame, 15)
        
        try:
            myBC.setPollFrame(15)
        except ValueError as myException:
            self.assertTrue(myException.args[0].startswith("BusController.setPollFrame:  "))
            
    '''
        Test: Call setPollFrame('a')
    '''
    def test_002_903_setPollFrame(self):
        myBC = BusController.BusController()
        
        self.assertRaises(ValueError, myBC.setPollFrame, 'a')
        
        try:
            myBC.setPollFrame('a')
        except ValueError as myException:
            self.assertTrue(myException.args[0].startswith("BusController.setPollFrame:  "))
            
    '''
        Test: Call setPollFrame([0])
    '''
    def test_002_904_setPollFrame(self):
        myBC = BusController.BusController()
        
        self.assertRaises(ValueError, myBC.setPollFrame, [0])
        
        try:
            myBC.setPollFrame([0])
        except ValueError as myException:
            self.assertTrue(myException.args[0].startswith("BusController.setPollFrame:  "))
            
    '''
        Test: Call setPollFrame([31])
    '''
    def test_002_905_setPollFrame(self):
        myBC = BusController.BusController()
        
        self.assertRaises(ValueError, myBC.setPollFrame, [31])
        
        try:
            myBC.setPollFrame([31])
        except ValueError as myException:
            self.assertTrue(myException.args[0].startswith("BusController.setPollFrame:  "))
            
    '''
        Test: Call setPollFrame([10.5]). A valid RT with address of 10 has been added to the satellite.
    '''
    def test_002_906_setPollFrame(self):
        myBC = BusController.BusController()
        mySat = Satellite.Satellite()
        myRT = RemoteTerminal.RemoteTerminal(10)
        
        mySat.addRemoteTerminal(myRT)        
        
        self.assertRaises(ValueError, myBC.setPollFrame, [10.5])
        
        try:
            myBC.setPollFrame([10.5])
        except ValueError as myException:
            self.assertTrue(myException.args[0].startswith("BusController.setPollFrame:  "))

            
    '''
        Test: Call setPollFrame([1.5]). A valid RT with address of 1 has been added to the satellite.
    '''
    def test_002_907_setPollFrame(self):
        myBC = BusController.BusController()
        mySat = Satellite.Satellite()
        myRT = RemoteTerminal.RemoteTerminal(1)
        
        mySat.addRemoteTerminal(myRT)
                
        self.assertRaises(ValueError, myBC.setPollFrame, [1.5])
        
        try:
            myBC.setPollFrame([1.5])
        except ValueError as myException:
            self.assertTrue(myException.args[0].startswith("BusController.setPollFrame:  "))

    '''
        Test: Call setPollFrame(['a'])
    '''
    def test_002_908_setPollFrame(self):
        myBC = BusController.BusController()
        
        self.assertRaises(ValueError, myBC.setPollFrame, ['a'])
        
        try:
            myBC.setPollFrame(['a'])
        except ValueError as myException:
            self.assertTrue(myException.args[0].startswith("BusController.setPollFrame:  "))
            
    '''
        Test: Call setPollFrame(['%'])
    '''
    def test_002_909_setPollFrame(self):
        myBC = BusController.BusController()
        
        self.assertRaises(ValueError, myBC.setPollFrame, ['%'])
        
        try:
            myBC.setPollFrame(['%'])
        except ValueError as myException:
            self.assertTrue(myException.args[0].startswith("BusController.setPollFrame:  "))
            
    '''
        Test: Call setPollFrame([10]), but do not associate it with any Satellite first.
    '''
    def test_002_910_setPollFrame(self):
        myBC = BusController.BusController()
        
        self.assertRaises(ValueError, myBC.setPollFrame, [10])
        
        try:
            myBC.setPollFrame([10])
        except ValueError as myException:
            self.assertTrue(myException.args[0].startswith("BusController.setPollFrame:  "))
            
    '''
        Test: Call setPollFrame([5, 10]). 5 is a valid Remote Terminal, but 10 is not. 
   ''' 
    def test_002_911_setPollFrame(self):
        myBC = BusController.BusController()
        mySat = Satellite.Satellite()
        myRT = RemoteTerminal.RemoteTerminal(5)
        
        mySat.setBusController(bc=myBC)
        
        mySat.addRemoteTerminal(myRT)
                
        self.assertRaises(ValueError, myBC.setPollFrame, [5, 10])
        
        try:
            myBC.setPollFrame([5, 10])
        except ValueError as myException:
            self.assertTrue(myException.args[0].startswith("BusController.setPollFrame:  "))
            
    '''
        Test: Call setPollFrame([5, 'a']). 5 is a valid Remote Terminal.
    '''
    def test_002_912_setPollFrame(self):
        myBC = BusController.BusController()
        mySat = Satellite.Satellite()
        myRT = RemoteTerminal.RemoteTerminal(5)
        
        mySat.setBusController(bc=myBC)
        
        mySat.addRemoteTerminal(myRT)
                
        self.assertRaises(ValueError, myBC.setPollFrame, [5, 'a'])
        
        try:
            myBC.setPollFrame([5, 'a'])
        except ValueError as myException:
            self.assertTrue(myException.args[0].startswith("BusController.setPollFrame:  "))


    '''
        Test: Assume rtList = [5, 5, 25] is valid. Call setPollFrame(rtList)
    '''
    def test_002_001_setPollFrame(self):
        myBC = BusController.BusController()
        mySat = Satellite.Satellite()
        
        remTerminal_5 = RemoteTerminal.RemoteTerminal(5)
        remTerminal_25 = RemoteTerminal.RemoteTerminal(25)
        
        mySat.setBusController(bc=myBC)
        
        mySat.addRemoteTerminal(remTerminal_5)
        mySat.addRemoteTerminal(remTerminal_25)
        
        rtList = [5, 5, 25]

        # TODO: May need to update this to three
        theResult = 3
        
        self.assertEquals(theResult, myBC.setPollFrame(rtList))
        
        self.assertEquals(theResult, myBC.setPollFrame(rtList=[5, 5, 25]))
        
        self.assertEquals([5, 5, 25], myBC.pollFrame)
        
    '''
        Test: Assume rtList = [25] is valid. Call setPollFrame(rtList)
    '''
    def test_002_002_setPollFrame(self):
        myBC = BusController.BusController()
        mySat = Satellite.Satellite()
        
        remTerminal_25 = RemoteTerminal.RemoteTerminal(25)

        mySat.setBusController(bc=myBC)

        mySat.addRemoteTerminal(rt=remTerminal_25)
        
        rtList = [25]
        
        theResult = 1
        
        self.assertEquals(theResult, myBC.setPollFrame(rtList))
        
        self.assertEquals(theResult, myBC.setPollFrame(rtList=[25]))
        
        self.assertEquals([25], myBC.pollFrame)
        
    '''
        Test: Assume rtList = [25, 25, 25] is valid. Call setPollFrame(rtList)
    '''
    def test_002_003_setPollFrame(self):
        myBC = BusController.BusController()
        mySat = Satellite.Satellite()
        
        remTerminal_25 = RemoteTerminal.RemoteTerminal(25)
        
        mySat.setBusController(bc=myBC)
        
        mySat.addRemoteTerminal(remTerminal_25)
        
        rtList = [25, 25, 25]
        
        theResult = 3
        
        self.assertEquals(theResult, myBC.setPollFrame(rtList))
        
        self.assertEquals(theResult, myBC.setPollFrame(rtList=[25, 25, 25]))
        
        self.assertEquals([25, 25, 25], myBC.pollFrame)
        
    '''
        Test: Create a satellite with 3 valid RTs on it. Call setPollFrame()
    '''
    def test_002_004_setPollFrame(self):
        myBC = BusController.BusController()
        mySat = Satellite.Satellite()
        
        remTerminal_25 = RemoteTerminal.RemoteTerminal(25)
        remTerminal_5 = RemoteTerminal.RemoteTerminal(5)
        remTerminal_2 = RemoteTerminal.RemoteTerminal(2)
        
        mySat.setBusController(bc=myBC)
        
        mySat.addRemoteTerminal(remTerminal_25)
        mySat.addRemoteTerminal(remTerminal_5)
        mySat.addRemoteTerminal(remTerminal_2)
        
        
        theResult = 0
        
        self.assertEquals(theResult, myBC.setPollFrame())
        
        self.assertEquals(theResult, myBC.setPollFrame(rtList=[]))
        
        self.assertEquals([], myBC.pollFrame)

    '''
        Test: Create a satellite with no valid RTs on it. Call setPollFrame()
    '''
    def test_002_005_setPollFrame(self):
        myBC = BusController.BusController()
        mySat = Satellite.Satellite()
   
        
        mySat.setBusController(bc=myBC)
        
        theResult = 0
        
        self.assertEquals(theResult, myBC.setPollFrame())
        
        self.assertEquals(theResult, myBC.setPollFrame(rtList=[]))
        
        self.assertEquals([], myBC.pollFrame)

    '''
        Test: Assume rtList = [1, 3, 4, 5, 25] is valid. Call setPollFrame(rtList)
    '''
    def test_002_006_setPollFrame(self):
        myBC = BusController.BusController()
        mySat = Satellite.Satellite()
        
        remTerminal_1 = RemoteTerminal.RemoteTerminal(1)
        remTerminal_3 = RemoteTerminal.RemoteTerminal(3)
        remTerminal_4 = RemoteTerminal.RemoteTerminal(4)
        remTerminal_5 = RemoteTerminal.RemoteTerminal(5)
        remTerminal_25 = RemoteTerminal.RemoteTerminal(25)
        
        mySat.setBusController(bc=myBC)

        mySat.addRemoteTerminal(remTerminal_1)
        mySat.addRemoteTerminal(remTerminal_3)
        mySat.addRemoteTerminal(remTerminal_4)
        mySat.addRemoteTerminal(remTerminal_5)
        mySat.addRemoteTerminal(remTerminal_25)
        
        rtList = [1, 3, 4, 5, 25]
        
        theResult = 5
        
        self.assertEquals(theResult, myBC.setPollFrame(rtList))
        
        self.assertEquals(theResult, myBC.setPollFrame(rtList=[1, 3, 4, 5, 25]))
        
        self.assertEquals([1, 3, 4, 5, 25], myBC.pollFrame)
        
# isValidRemoteTerminalList

    '''
        Test: Check different inputs to make sure isValidRemoteTerminalList returns the correct value.
    '''
    def test_003_001_isValidRemoteTerminalList(self):
        myBC = BusController.BusController()
        
        myList = [1, 2, 3]
        self.assertTrue(myBC.isValidRemoteTerminalList(rtList=myList))
        
        myList = [1, 20, 30]
        self.assertTrue(myBC.isValidRemoteTerminalList(rtList=myList))
        
        myList = []
        self.assertTrue(myBC.isValidRemoteTerminalList(rtList=myList))
        
        myList = [1]
        self.assertTrue(myBC.isValidRemoteTerminalList(rtList=myList))
        
        myList = [30]
        self.assertTrue(myBC.isValidRemoteTerminalList(rtList=myList))

        myList = [31]
        self.assertFalse(myBC.isValidRemoteTerminalList(rtList=myList))
        
        myList = [0]
        self.assertFalse(myBC.isValidRemoteTerminalList(rtList=myList))
        
        myList = [5, 10, 31]
        self.assertFalse(myBC.isValidRemoteTerminalList(rtList=myList))
        
        myList = [5, 8, 0]
        self.assertFalse(myBC.isValidRemoteTerminalList(rtList=myList))
        
        myList = [6, 25, 'a']
        self.assertFalse(myBC.isValidRemoteTerminalList(rtList=myList))
        
        myList = ['a']
        self.assertFalse(myBC.isValidRemoteTerminalList(rtList=myList))
        
# countUniqueAddresses

    '''
        Test: Check different inputs to make sure isValidRemoteTerminalList returns the correct value.
    '''
    def test_004_001_countUniqueAddresses(self):
        myBC = BusController.BusController()
        
        myList = [1, 2, 3]
        self.assertEquals(3, myBC.countUniqueAddresses(rtList=myList))
        
        myList = [1, 20, 30]
        self.assertEquals(3, myBC.countUniqueAddresses(rtList=myList))
        
        myList = []
        self.assertEquals(0, myBC.countUniqueAddresses(rtList=myList))
        
        myList = [1]
        self.assertEquals(1, myBC.countUniqueAddresses(rtList=myList))
        
        myList = [30]
        self.assertEquals(1, myBC.countUniqueAddresses(rtList=myList))
        
        myList = [1, 1, 2, 30, 30]
        self.assertEquals(3, myBC.countUniqueAddresses(rtList=myList))
        
        myList = [30, 30, 30, 30, 30]
        self.assertEquals(1, myBC.countUniqueAddresses(rtList=myList))

# poll

    '''
        Test: Set up a valid BusController attached to a Satellite with no remote terminals. Call poll()
    '''
    def test_005_001_poll(self):
        myBC = BusController.BusController()
        mySat = Satellite.Satellite()
        
        mySat.setBusController(myBC)
        
        self.assertEquals(0, myBC.poll())

    '''
        Test: Set up a valid BusController attached to a Satellite with 1 remote terminal. 
        Poll Frame is empty. Call poll()
    '''
    def test_005_002_poll(self):
        print "\n----------Starting Test test_005_002_poll----------"
        
        status_1_counter = 0
        status_2_counter = 0
        vector_1_counter = 0
        vector_2_counter = 0
        vector_3_counter = 0
        vector_4_counter = 0
        
        testLoops = 1000
        for testIndex in range(0, testLoops):
        
            myBC = BusController.BusController()
            mySat = Satellite.Satellite()
            myRemTerm = RemoteTerminal.RemoteTerminal(1)
            
            mySat.setBusController(myBC)
            mySat.addRemoteTerminal(myRemTerm)
            
            # Poll Frame is left empty, but will be set when poll is called
            
            self.assertEquals(1, myBC.poll())
            self.assertEquals([1], myBC.pollFrame)
            
            status_1_counter = status_1_counter + myBC.getTestCounter("test_status_normal")
            status_2_counter = status_2_counter + myBC.getTestCounter("test_status_service")
            vector_1_counter = vector_1_counter + myBC.getTestCounter("test_vector_status")
            vector_2_counter = vector_2_counter + myBC.getTestCounter("test_vector_receive")
            vector_3_counter = vector_3_counter + myBC.getTestCounter("test_vector_transmit")
            vector_4_counter = vector_4_counter + myBC.getTestCounter("test_vector_vector")
        
        self.assertAlmostEquals((float)(status_1_counter) / testLoops, 0.5, None, None, 0.05)
        self.assertAlmostEquals((float)(status_2_counter) / testLoops, 0.5, None, None, 0.05)
        # Note: Because there is a 50% chance of none of the below situations happening there is really a 12% (50% * 25%)
        self.assertAlmostEquals((float)(vector_1_counter) / testLoops, 0.125, None, None, 0.05)
        self.assertAlmostEquals((float)(vector_2_counter) / testLoops, 0.125, None, None, 0.05)
        self.assertAlmostEquals((float)(vector_3_counter) / testLoops, 0.125, None, None, 0.05)
        self.assertAlmostEquals((float)(vector_4_counter) / testLoops, 0.125, None, None, 0.05)
        
    '''
        Test: Set up a valid BusController attached to a Satellite with 1 remote terminal. 
        Poll Frame is empty. Call poll()
    '''
    def test_005_003_poll(self):
        print "\n----------Starting Test test_005_003_poll----------"
        myBC = BusController.BusController()
        mySat = Satellite.Satellite()
        myRemTerm_1 = RemoteTerminal.RemoteTerminal(1)
        myRemTerm_2 = RemoteTerminal.RemoteTerminal(2)
        
        mySat.setBusController(myBC)
        mySat.addRemoteTerminal(myRemTerm_1)
        mySat.addRemoteTerminal(myRemTerm_2)
        
        timesPolled = 2
        
        # Poll Frame is left empty, but will be set when poll is called
        
        self.assertEquals(timesPolled, myBC.poll())
        self.assertEquals([1, 2], myBC.pollFrame)
        
    '''
        Test: Set up a valid BusController attached to a Satellite 
        with 2 remote terminal. Poll Frame is [2, 1]. Call poll()
    '''
    def test_005_004_poll(self):
        print "\n----------Starting Test test_005_004_poll----------"
        myBC = BusController.BusController()
        mySat = Satellite.Satellite()
        myRemTerm_1 = RemoteTerminal.RemoteTerminal(1)
        myRemTerm_2 = RemoteTerminal.RemoteTerminal(2)
        
        mySat.setBusController(myBC)
        mySat.addRemoteTerminal(myRemTerm_1)
        mySat.addRemoteTerminal(myRemTerm_2)
        
        myBC.setPollFrame([2, 1])
        
        timesPolled = 2
                
        self.assertEquals(timesPolled, myBC.poll())
        self.assertEquals([2, 1], myBC.pollFrame)
        
    '''
        Test: Set up a valid BusController attached to a Satellite 
        with 2 remote terminal. Poll Frame is [2]. Call poll()
    '''
    def test_005_005_poll(self):
        print "\n----------Starting Test test_005_005_poll----------"
        myBC = BusController.BusController()
        mySat = Satellite.Satellite()
        myRemTerm_1 = RemoteTerminal.RemoteTerminal(1)
        myRemTerm_2 = RemoteTerminal.RemoteTerminal(2)
        
        mySat.setBusController(myBC)
        mySat.addRemoteTerminal(myRemTerm_1)
        mySat.addRemoteTerminal(myRemTerm_2)
        
        myBC.setPollFrame([2])
        
        timesPolled = 1
                
        self.assertEquals(timesPolled, myBC.poll())
        self.assertEquals([2], myBC.pollFrame)
        
    '''
        Test: Set up a valid BusController attached to a Satellite 
        with 2 remote terminals. Poll Frame is [5, 2, 5]. Call poll()
    '''
    def test_005_006_poll(self):
        print "\n----------Starting Test test_005_006_poll----------"
        myBC = BusController.BusController()
        mySat = Satellite.Satellite()
        myRemTerm_1 = RemoteTerminal.RemoteTerminal(5)
        myRemTerm_2 = RemoteTerminal.RemoteTerminal(2)
        
        mySat.setBusController(myBC)
        mySat.addRemoteTerminal(myRemTerm_1)
        mySat.addRemoteTerminal(myRemTerm_2)
        
        myBC.setPollFrame([5, 2, 5])
        
        timesPolled = 3
                
        self.assertEquals(timesPolled, myBC.poll())
        self.assertEquals([5, 2, 5], myBC.pollFrame)

    '''
        Test: Set up a valid BusController attached to a Satellite with 
        4 remote terminals. Poll Frame is [3, 8, 4, 10, 10]. Call poll()
    '''
    def test_005_007_poll(self):
        print "\n----------Starting Test test_005_007_poll----------"
        myBC = BusController.BusController()
        mySat = Satellite.Satellite()
        myRemTerm_1 = RemoteTerminal.RemoteTerminal(4)
        myRemTerm_2 = RemoteTerminal.RemoteTerminal(3)
        myRemTerm_3 = RemoteTerminal.RemoteTerminal(8)
        myRemTerm_4 = RemoteTerminal.RemoteTerminal(10)
        
        mySat.setBusController(myBC)
        mySat.addRemoteTerminal(myRemTerm_1)
        mySat.addRemoteTerminal(myRemTerm_2)
        mySat.addRemoteTerminal(myRemTerm_3)
        mySat.addRemoteTerminal(myRemTerm_4)
        
        myBC.setPollFrame([3, 8, 4, 10, 10])
        
        timesPolled = 5
                
        self.assertEquals(timesPolled, myBC.poll())
        self.assertEquals([3, 8, 4, 10, 10], myBC.pollFrame)
        
    '''
        Test: Set up a valid BusController attached to a Satellite with 
        5 remote terminals. Add the terminals in order: 3, 4, 5, 2, 1. 
        Poll Frame is []. Call poll()
    '''
    def test_005_008_poll(self):
        print "\n----------Starting Test test_005_007_poll----------"
        
        status_1_counter = 0
        status_2_counter = 0
        vector_1_counter = 0
        vector_2_counter = 0
        vector_3_counter = 0
        vector_4_counter = 0
        
        testLoops = 1000
        for testIndex in range(0, testLoops):
            
            myBC = BusController.BusController()
            mySat = Satellite.Satellite()
            myRemTerm_1 = RemoteTerminal.RemoteTerminal(3)
            myRemTerm_2 = RemoteTerminal.RemoteTerminal(4)
            myRemTerm_3 = RemoteTerminal.RemoteTerminal(5)
            myRemTerm_4 = RemoteTerminal.RemoteTerminal(2)
            myRemTerm_5 = RemoteTerminal.RemoteTerminal(1)
            
            mySat.setBusController(myBC)
            mySat.addRemoteTerminal(myRemTerm_1)
            mySat.addRemoteTerminal(myRemTerm_2)
            mySat.addRemoteTerminal(myRemTerm_3)
            mySat.addRemoteTerminal(myRemTerm_4)
            mySat.addRemoteTerminal(myRemTerm_5)
            
            myBC.setPollFrame([])
        
            timesPolled = 5
        
            # Poll Frame is left empty, but will be set when poll is called
        
            self.assertEquals(timesPolled, myBC.poll())
            self.assertEquals([1, 2, 3, 4, 5], myBC.pollFrame)
        
            status_1_counter = status_1_counter + myBC.getTestCounter("test_status_normal")
            status_2_counter = status_2_counter + myBC.getTestCounter("test_status_service")
            vector_1_counter = vector_1_counter + myBC.getTestCounter("test_vector_status")
            vector_2_counter = vector_2_counter + myBC.getTestCounter("test_vector_receive")
            vector_3_counter = vector_3_counter + myBC.getTestCounter("test_vector_transmit")
            vector_4_counter = vector_4_counter + myBC.getTestCounter("test_vector_vector")
        
        self.assertAlmostEquals((float)(status_1_counter) / testLoops / 5, 0.5, None, None, 0.05)
        self.assertAlmostEquals((float)(status_2_counter) / testLoops / 5, 0.5, None, None, 0.05)
        # Note: Because there is a 50% chance of none of the below situations happening there is really a 12% (50% * 25%)
        self.assertAlmostEquals((float)(vector_1_counter) / testLoops / 5, 0.125, None, None, 0.05)
        self.assertAlmostEquals((float)(vector_2_counter) / testLoops / 5, 0.125, None, None, 0.05)
        self.assertAlmostEquals((float)(vector_3_counter) / testLoops / 5, 0.125, None, None, 0.05)
        self.assertAlmostEquals((float)(vector_4_counter) / testLoops / 5, 0.125, None, None, 0.05)











