'''
    Created on Apr 20, 2014
    Last updated on Apr 20, 2014

    This is a test file used to test the Satellite Class

    @author: Andrew K. Marshall
'''
import unittest

import prod.RemoteTerminal as RemoteTerminal
import prod.BusController as BusController
import prod.Satellite as Satellite


class Test(unittest.TestCase):

# Satellite
# methods: instantiate, setBusController(bc), addRemoteTerminal(rt), getBusController(), 
#          getRemoteTerminals(), launch(frameCount)

# Constructor

    '''
        Test: Instantiate Satellite()
    '''
    def test_001_001_InstantiateStaellite(self):
        mySatellite = Satellite.Satellite()
        
        self.assertTrue(isinstance(mySatellite, Satellite.Satellite))
        self.assertEquals(mySatellite.subsystemsList, [])

# addRemoteTerminal

    '''
        Test: Create a valid Satellite. Create a valid Remote Terminal RT. Call addRemoteTerminal(rt=RT)
    '''
    def test_002_001_addRemoteTerminal(self):
        mySatellite = Satellite.Satellite()

        myRemTerminal_1 = RemoteTerminal.RemoteTerminal(1)
        
        theResult = 1
        
        self.assertEquals(theResult, mySatellite.addRemoteTerminal(rt=myRemTerminal_1))
        self.assertEquals(mySatellite.subsystemsList, [myRemTerminal_1])
        
    '''
        Test: Create a valid Satellite. Create a valid Remote Terminal RT. Call addRemoteTerminal(RT)
    '''
    def test_002_002_addRemoteTerminal(self):
        mySatellite = Satellite.Satellite()

        myRemTerminal_1 = RemoteTerminal.RemoteTerminal(1)
        
        theResult = 1
        
        self.assertEquals(theResult, mySatellite.addRemoteTerminal(myRemTerminal_1))
        self.assertEquals(mySatellite.subsystemsList, [myRemTerminal_1])
        
    '''
        Test: Create a valid Satellite. Create 30 valid Remote Terminals RT1 - 30. 
        Call addRemoteTerminal(rt=RT1-30) 30 times.
    '''
    def test_003_003_addRemoteTerminal(self):
        mySatellite = Satellite.Satellite()
        
        # Create 30 Remote Terminals
        for testLoopIndex in range(1, 31):
            
            tempRemoteTerminal = RemoteTerminal.RemoteTerminal(testLoopIndex)
            
            self.assertEquals(testLoopIndex, mySatellite.addRemoteTerminal(rt=tempRemoteTerminal))
            
    '''
        Test: Create a valid Satellite. Create 30 valid Remote Terminals RT1 - 30. 
        Call addRemoteTerminal(rt=RT1-30) 30 times. Try to add 1 more.
    '''
    def test_003_901_addRemoteTerminal(self):
        mySatellite = Satellite.Satellite()
        
        # Create 30 Remote Terminals
        for testLoopIndex in range(1, 31):
            
            tempRemoteTerminal = RemoteTerminal.RemoteTerminal(testLoopIndex)
            
            self.assertEquals(testLoopIndex, mySatellite.addRemoteTerminal(rt=tempRemoteTerminal))
            
        remoteTerminal = RemoteTerminal.RemoteTerminal(30)
            
        self.assertRaises(ValueError, mySatellite.addRemoteTerminal, rt=remoteTerminal)

        try:
            mySatellite.addRemoteTerminal(rt=remoteTerminal)
        except ValueError as myException:
            self.assertTrue(myException.args[0].startswith("Satellite.addRemoteTerminal:  "))
            
    '''
        Test: Create a valid Satellite. Create a valid Remote Terminal RT. 
        Call addRemoteTerminal(rt=RT) twice. 
    '''
    def test_003_902_addRemoteTerminal(self):
        mySatellite = Satellite.Satellite()
           
        tempRemoteTerminal = RemoteTerminal.RemoteTerminal(5)
            
        self.assertEquals(1, mySatellite.addRemoteTerminal(rt=tempRemoteTerminal))
                        
        self.assertRaises(ValueError, mySatellite.addRemoteTerminal, rt=tempRemoteTerminal)

        try:
            mySatellite.addRemoteTerminal(rt=tempRemoteTerminal)
        except ValueError as myException:
            self.assertTrue(myException.args[0].startswith("Satellite.addRemoteTerminal:  "))
            
    '''
        Test: Create a valid Satellite. Create 2 valid Remote Terminals RT1 and RT2. 
        Call addRemoteTerminal(rt=RT1), then call addRemoteTerminal(RT2). 
        Then call addRemoteTermainl(RT1).
    '''
    def test_003_903_addRemoteTerminal(self):
        mySatellite = Satellite.Satellite()
           
        myRemoteTerminal_1 = RemoteTerminal.RemoteTerminal(5)
        myRemoteTerminal_2 = RemoteTerminal.RemoteTerminal(10)
        
        self.assertEquals(1, mySatellite.addRemoteTerminal(rt=myRemoteTerminal_1))
        
        self.assertEquals(2, mySatellite.addRemoteTerminal(rt=myRemoteTerminal_2))
                        
        self.assertRaises(ValueError, mySatellite.addRemoteTerminal, rt=myRemoteTerminal_1)

        try:
            mySatellite.addRemoteTerminal(rt=myRemoteTerminal_1)
        except ValueError as myException:
            self.assertTrue(myException.args[0].startswith("Satellite.addRemoteTerminal:  "))
            
    '''
        Test: Create a valid Satellite. Call addRemoteTerminal(rt=5)
    '''
    def test_003_904_addRemoteTerminal(self):
        mySatellite = Satellite.Satellite()
                                                   
        self.assertRaises(ValueError, mySatellite.addRemoteTerminal, rt=5)

        try:
            mySatellite.addRemoteTerminal(rt=5)
        except ValueError as myException:
            self.assertTrue(myException.args[0].startswith("Satellite.addRemoteTerminal:  "))
            
    '''
        Test: Create a valid Satellite. Call addRemoteTerminal(5)
    '''
    def test_003_905_addRemoteTerminal(self):
        mySatellite = Satellite.Satellite()
                                                   
        self.assertRaises(ValueError, mySatellite.addRemoteTerminal, 5)

        try:
            mySatellite.addRemoteTerminal(5)
        except ValueError as myException:
            self.assertTrue(myException.args[0].startswith("Satellite.addRemoteTerminal:  "))
            
    '''
        Test: Create a valid Satellite. Call addRemoteTerminal(rt='a')
    '''
    def test_003_906_addRemoteTerminal(self):
        mySatellite = Satellite.Satellite()
                                                   
        self.assertRaises(ValueError, mySatellite.addRemoteTerminal, rt='a')

        try:
            mySatellite.addRemoteTerminal(rt='a')
        except ValueError as myException:
            self.assertTrue(myException.args[0].startswith("Satellite.addRemoteTerminal:  "))
            
    '''
        Test: Create a valid Satellite. Call addRemoteTerminal('%')
    '''
    def test_003_907_addRemoteTerminal(self):
        mySatellite = Satellite.Satellite()
                                                   
        self.assertRaises(ValueError, mySatellite.addRemoteTerminal, '%')

        try:
            mySatellite.addRemoteTerminal('%')
        except ValueError as myException:
            self.assertTrue(myException.args[0].startswith("Satellite.addRemoteTerminal:  "))
            
# getRemoteTerminals

    '''
        Test: Create a valid Satellite with no Remote Terminals attached. Call getRemoteTerminals()
    '''
    def test_004_001_getRemoteTerminals(self):
        mySatellite = Satellite.Satellite()
        
        theResult = []
        
        self.assertEquals(theResult, mySatellite.getRemoteTerminals())
        self.assertEquals(theResult, mySatellite.getRemoteTerminalAddresses())
        
    '''
        Test: Create a valid Satellite with 1 Remote Terminal attached. Call getRemoteTerminals()
    '''
    def test_004_002_getRemoteTerminals(self):
        mySatellite = Satellite.Satellite()
        
        myRemoteTerminal = RemoteTerminal.RemoteTerminal(5)
        
        mySatellite.addRemoteTerminal(myRemoteTerminal)
        
        theResult = [myRemoteTerminal]
        
        self.assertEquals(theResult, mySatellite.getRemoteTerminals())
        self.assertEquals([5], mySatellite.getRemoteTerminalAddresses())
        
    '''
        Test: Create a valid Satellite with 30 Remote Terminal attached. Call getRemoteTerminals()
    '''
    def test_004_003_getRemoteTerminals(self):
        mySatellite = Satellite.Satellite()
        
        theResult = []
        theResult2 = []
        
        # Create 30 Remote Terminals
        for testLoopIndex in range(1, 31):
            
            tempRemoteTerminal = RemoteTerminal.RemoteTerminal(testLoopIndex)
        
            mySatellite.addRemoteTerminal(tempRemoteTerminal)
        
            theResult.append(tempRemoteTerminal)
            theResult2.append(tempRemoteTerminal.getAddress())
        
        self.assertEquals(theResult, mySatellite.getRemoteTerminals())
        self.assertEquals(theResult2, mySatellite.getRemoteTerminalAddresses())
        
# setBusController

    '''
        Test: Call setBusController(bc='a')
    '''
    def test_005_901_setBusController(self):
        mySat = Satellite.Satellite()
        
        self.assertRaises(ValueError, mySat.setBusController, bc='a')

        try:
            mySat.setBusController(bc='a')
        except ValueError as myException:
            self.assertTrue(myException.args[0].startswith("Satellite.setBusController:  "))
            
    '''
        Test: Call setBusController(bc='1')
    '''
    def test_005_902_setBusController(self):
        mySat = Satellite.Satellite()
        
        self.assertRaises(ValueError, mySat.setBusController, bc='1')

        try:
            mySat.setBusController(bc='1')
        except ValueError as myException:
            self.assertTrue(myException.args[0].startswith("Satellite.setBusController:  "))
            
    '''
        Test: Call setBusController(bc=None)
    '''
    def test_005_903_setBusController(self):
        mySat = Satellite.Satellite()
        
        self.assertRaises(ValueError, mySat.setBusController, bc=None)

        try:
            mySat.setBusController(bc=None)
        except ValueError as myException:
            self.assertTrue(myException.args[0].startswith("Satellite.setBusController:  "))
            
    '''
        Test: Call setBusController(1)
    '''
    def test_005_904_setBusController(self):
        mySat = Satellite.Satellite()
        
        self.assertRaises(ValueError, mySat.setBusController, 1)

        try:
            mySat.setBusController(1)
        except ValueError as myException:
            self.assertTrue(myException.args[0].startswith("Satellite.setBusController:  "))
            
    '''
        Test: Call setBusController('a')
    '''
    def test_005_905_setBusController(self):
        mySat = Satellite.Satellite()
        
        self.assertRaises(ValueError, mySat.setBusController, 'a')

        try:
            mySat.setBusController('a')
        except ValueError as myException:
            self.assertTrue(myException.args[0].startswith("Satellite.setBusController:  "))
            
    '''
        Test: Create a valid Bus Controller, BC. Call setBusController(bc=BC).
    '''
    def test_005_001_setBusController(self):
        mySat = Satellite.Satellite()
        myBC = BusController.BusController()
        
        theResult = True
        
        self.assertEquals(theResult, mySat.setBusController(bc=myBC))
        
        self.assertEquals(mySat, myBC.linkedSatellite)
        
           
    '''
        Test: Create a valid Bus Controller, BC. Call setBusController(BC).
    '''
    def test_005_002_setBusController(self):
        mySat = Satellite.Satellite()
        myBC = BusController.BusController()
        
        theResult = True
        
        self.assertEquals(theResult, mySat.setBusController(myBC))
        
    '''
        Test: Create 2 valid Bus Controllers, BC1 and BC2. 
        Call setBusController(bc=BC1) then call setBusController(bc=BC2)
    '''
    def test_005_003_setBusController(self):
        mySat = Satellite.Satellite()
        myBC = BusController.BusController()
        myBC2 = BusController.BusController()
        
        theResult = True
        theResult2 = False
        
        self.assertEquals(theResult, mySat.setBusController(bc=myBC))
        self.assertEquals(mySat, myBC.linkedSatellite)
        self.assertEquals(theResult2, mySat.setBusController(bc=myBC2))
        self.assertEquals(mySat, myBC2.linkedSatellite)
        
    '''
        Test: Create 2 valid Bus Controllers, BC1 and BC2. 
        Call setBusController(BC1) then call setBusController(BC2)
    '''
    def test_005_004_setBusController(self):
        mySat = Satellite.Satellite()
        myBC = BusController.BusController()
        myBC2 = BusController.BusController()
        
        theResult = True
        theResult2 = False
        
        self.assertEquals(theResult, mySat.setBusController(myBC))
        self.assertEquals(mySat, myBC.linkedSatellite)
        self.assertEquals(theResult2, mySat.setBusController(myBC2))
        self.assertEquals(mySat, myBC2.linkedSatellite)
        
    '''
        Test: Create a valid Bus Controller, BC. Call setBusController(bc=BC). 
        Then call setBusController(%)
    '''
    def test_005_906_setBusController(self):
        mySat = Satellite.Satellite()
        myBC = BusController.BusController()

        self.assertEquals(True, mySat.setBusController(myBC))
        
        self.assertRaises(ValueError, mySat.setBusController, '%')

        try:
            mySat.setBusController('%')
        except ValueError as myException:
            self.assertTrue(myException.args[0].startswith("Satellite.setBusController:  "))
            
# getBusController

    '''
        Test: Create a valid Satellite. Call getBusController().
    '''
    def test_006_901_getBusController(self):
        mySat = Satellite.Satellite()
        
        self.assertRaises(ValueError, mySat.getBusController)

        try:
            mySat.getBusController()
        except ValueError as myException:
            self.assertTrue(myException.args[0].startswith("Satellite.getBusController:  "))

    '''
        Test: Create a valid Satellite. Set a valid Bus Controller, BC1. Call getBusController().
    '''
    def test_006_001_getBusController(self):
        mySat = Satellite.Satellite()
        
        myBC = BusController.BusController()
        myBC2 = BusController.BusController()
        
        mySat.setBusController(bc=myBC)
        
        self.assertEquals(myBC, mySat.getBusController())
        
    '''
        Test: Create 2 valid Bus Controllers, BC1 and BC2. 
        Call setBusController(bc=BC1) then call setBusController(bc=BC2). 
        Call getBusController()
    '''
    def test_006_002_getBusController(self):
        mySat = Satellite.Satellite()
        
        myBC = BusController.BusController()
        myBC2 = BusController.BusController()
        
        mySat.setBusController(bc=myBC)
        
        self.assertEquals(myBC, mySat.getBusController())
        
        mySat.setBusController(bc=myBC2)
        
        self.assertEquals(myBC2, mySat.getBusController())

# launch

    '''
        Test: Create a valid Satellite. Call launch(-1).
    '''
    def test_007_901_launch(self):
        mySat = Satellite.Satellite()
        
        self.assertRaises(ValueError, mySat.launch, -1)

        try:
            mySat.launch(-1)
        except ValueError as myException:
            self.assertTrue(myException.args[0].startswith("Satellite.launch:  "))
            
    '''
        Test: Create a valid Satellite. Call launch(frameCount=-1).
    '''
    def test_007_902_launch(self):
        mySat = Satellite.Satellite()
        
        self.assertRaises(ValueError, mySat.launch, frameCount=-1)

        try:
            mySat.launch(frameCount=-1)
        except ValueError as myException:
            self.assertTrue(myException.args[0].startswith("Satellite.launch:  "))
            
    '''
        Test: Create a valid Satellite. Call launch(frameCount='a').
    '''
    def test_007_903_launch(self):
        mySat = Satellite.Satellite()
        
        self.assertRaises(ValueError, mySat.launch, frameCount='a')

        try:
            mySat.launch(frameCount='a')
        except ValueError as myException:
            self.assertTrue(myException.args[0].startswith("Satellite.launch:  "))
            
    '''
        Test: Create a valid Satellite. Call launch('a').
    '''
    def test_007_904_launch(self):
        mySat = Satellite.Satellite()
        
        self.assertRaises(ValueError, mySat.launch,'a')

        try:
            mySat.launch('a')
        except ValueError as myException:
            self.assertTrue(myException.args[0].startswith("Satellite.launch:  "))
            
    '''
        Test: Create a valid Satellite. Call launch(frameCount='$').
    '''
    def test_007_905_launch(self):
        mySat = Satellite.Satellite()
        
        self.assertRaises(ValueError, mySat.launch, frameCount='$')

        try:
            mySat.launch(frameCount='$')
        except ValueError as myException:
            self.assertTrue(myException.args[0].startswith("Satellite.launch:  "))
            
    '''
        Test: Create a valid Satellite. Call launch(10.5).
    '''
    def test_007_906_launch(self):
        mySat = Satellite.Satellite()
        
        self.assertRaises(ValueError, mySat.launch,10.5)

        try:
            mySat.launch(10.5)
        except ValueError as myException:
            self.assertTrue(myException.args[0].startswith("Satellite.launch:  "))
            
    '''
        Test: Create a valid Satellite. With a valid Bus Controller attached 
        and some valid Terminals. Call launch()
    '''
    def test_007_006_launch(self):
        mySat = Satellite.Satellite()
        myBC = BusController.BusController()
        
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

        wordsWritten = mySat.launch()

        print "Words Written To Bus:"
        print wordsWritten
        
    '''
        Test: Create a valid Satellite. With a valid Bus Controller attached 
        and some valid Terminals. Call launch(frameCount=1)
    '''
    def test_007_005_launch(self):
        mySat = Satellite.Satellite()
        myBC = BusController.BusController()
        
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

        wordsWritten = mySat.launch(frameCount=1)

        print "Words Written To Bus:"
        print wordsWritten
        
    '''
        Test: Create a valid Satellite. With a valid Bus Controller attached 
        and some valid Terminals. Call launch(frameCount=10)
    '''
    def test_007_004_launch(self):
        mySat = Satellite.Satellite()
        myBC = BusController.BusController()
        
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

        wordsWritten = mySat.launch(frameCount=10)

        print "Words Written To Bus:"
        print wordsWritten
        
    '''
        Test: Create a valid Satellite. With a valid Bus Controller attached 
        and some valid Terminals. Call launch(10)
    '''
    def test_007_003_launch(self):
        mySat = Satellite.Satellite()
        myBC = BusController.BusController()
        
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

        wordsWritten = mySat.launch(10)

        print "Words Written To Bus:"
        print wordsWritten
        
    '''
        Test: Create a valid Satellite. With a valid Bus Controller attached 
        and some valid Terminals. Call launch(100)
    '''
    def test_007_002_launch(self):
        mySat = Satellite.Satellite()
        myBC = BusController.BusController()
        
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

        wordsWritten = mySat.launch(100)

        print "Words Written To Bus:"
        print wordsWritten
        
    '''
        Test: Create a valid Satellite. With a valid Bus Controller attached 
        and some valid Terminals. Call launch(frameCount=100)
    '''
    def test_007_001_launch(self):
        mySat = Satellite.Satellite()
        myBC = BusController.BusController()
        
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

        wordsWritten = mySat.launch(frameCount=100)

        print "Words Written To Bus:"
        print wordsWritten





















