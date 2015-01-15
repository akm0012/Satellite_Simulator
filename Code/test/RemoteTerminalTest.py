'''
    Created on Apr 5, 2014
    Last updated on Apr 6, 2014

    This is a test file used to test the RemoteTerminal Class

    @author: Andrew K. Marshall
'''
import unittest

import prod.Bus as bus
import prod.Command as command
import prod.Status as status
import prod.Data as data
import prod.RemoteTerminal as remoteTerminal

class remoteTerminalTest(unittest.TestCase):

# RemoteTerminal
# methods: instantiate, readBus(bus), getAddress() 

    ''' 
        Called before every method.  Creates a valid word instance of a Command, Data, and Status.
    '''
    
    def setUp(self):
        self.myCommandWord = command.Command(1)
        self.myStatusWord = status.Status(15)
        self.myDataWord = data.Data(20)

# Constructor 
    '''
        Test: Instantiate RemoteTerminal(1)
    '''
    def test_001_001_InstantiateStatus(self):
        myRemoteTerminal = remoteTerminal.RemoteTerminal(1)
        
        theResult1 = True
        theResult2 = 1
        
        self.assertEquals(theResult1, isinstance(myRemoteTerminal, remoteTerminal.RemoteTerminal))
        self.assertEquals(theResult2, myRemoteTerminal.address)
        
    '''
        Test: Instantiate RemoteTerminal(15)
    '''
    def test_001_002_InstantiateStatus(self):
        myRemoteTerminal = remoteTerminal.RemoteTerminal(15)
        
        theResult1 = True
        theResult2 = 15
        
        self.assertEquals(theResult1, isinstance(myRemoteTerminal, remoteTerminal.RemoteTerminal))
        self.assertEquals(theResult2, myRemoteTerminal.address)
        
    '''
        Test: Instantiate RemoteTerminal(30)
    '''
    def test_001_003_InstantiateStatus(self):
        myRemoteTerminal = remoteTerminal.RemoteTerminal(30)
        
        theResult1 = True
        theResult2 = 30
        
        self.assertEquals(theResult1, isinstance(myRemoteTerminal, remoteTerminal.RemoteTerminal))
        self.assertEquals(theResult2, myRemoteTerminal.address)
    
    '''
        Test: Instantiate RemoteTerminal(31)
    '''
    def test_001_901_InstantiateStatus(self):
        self.assertRaises(ValueError, remoteTerminal.RemoteTerminal, 31)
        
    '''
        Test: Instantiate RemoteTerminal(0)
    '''
    def test_001_902_InstantiateStatus(self):
        self.assertRaises(ValueError, remoteTerminal.RemoteTerminal, 0)
        
    '''
        Test: Instantiate RemoteTerminal('a')
    '''
    def test_001_903_InstantiateStatus(self):
        self.assertRaises(ValueError, remoteTerminal.RemoteTerminal, 'a')
        
    '''
        Test: Instantiate RemoteTerminal('$')
    '''
    def test_001_904_InstantiateStatus(self):
        self.assertRaises(ValueError, remoteTerminal.RemoteTerminal, '$')
        
# getAddress

    '''
        Test: RemoteTerminal(15).getAddress()
    '''
    def test_002_001_getAddress(self): 
        myRemoteTerminal = remoteTerminal.RemoteTerminal(15)
            
        theResult = 15
            
        self.assertEquals(theResult, myRemoteTerminal.getAddress())
        
    '''
        Test: RemoteTerminal(1).getAddress()
    '''
    def test_002_002_getAddress(self): 
        myRemoteTerminal = remoteTerminal.RemoteTerminal(1)
            
        theResult = 1
            
        self.assertEquals(theResult, myRemoteTerminal.getAddress())
        
    '''
        Test: RemoteTerminal(30).getAddress()
    '''
    def test_002_003_getAddress(self): 
        myRemoteTerminal = remoteTerminal.RemoteTerminal(30)
            
        theResult = 30
            
        self.assertEquals(theResult, myRemoteTerminal.getAddress())
        
# readBus

    '''
        Test: Instantiate RemoteTerminal(1). Call readBus('a')
    '''
    def test_003_901_readBus(self):
        myRemoteTerminal = remoteTerminal.RemoteTerminal(15)
        
        self.assertRaises(ValueError, myRemoteTerminal.readBus, 'a')
        
    '''
        Test: Instantiate RemoteTerminal(1). Call readBus(1)
    '''
    def test_003_902_readBus(self):
        myRemoteTerminal = remoteTerminal.RemoteTerminal(1)
        
        self.assertRaises(ValueError, myRemoteTerminal.readBus, 1)
        
    '''
        Test: Instantiate RemoteTerminal(1). Call readBus(RemoteTerminal)
    '''
    def test_003_903_readBus(self):
        myRemoteTerminal = remoteTerminal.RemoteTerminal(1)
        myRemoteTerminal_other = remoteTerminal.RemoteTerminal(15)
        
        self.assertRaises(ValueError, myRemoteTerminal.readBus, myRemoteTerminal_other)
        
    '''
        Test: Remote Terminal: Scenario 1: Request status from the remote terminal
    '''
    def test_003_001_readBus_scenario_1(self):
        
        # Because responceBus has a 50/50 chance of having serviceRequestFlag set to True
        # we will run this multiple times and make sure we see both the true and false values
        probability_50_50_check_1 = False
        probability_50_50_check_2 = False
        
        for testLoopIndex in range(0, 200):
            # Create instance of Remote Terminal 
            remTermAddress = 4
            remTerm = remoteTerminal.RemoteTerminal(remTermAddress)
            
            # Set up the Command that will request status
            myCommand = command.Command(remTerm.getAddress())
            myCommand.setToModeCommand(command.Command.transmitStatusWord)
            
            # Write the Command to the Bus
            myBus = bus.Bus()
            myBus.writeBus(myCommand)
            
            returnedBus = remTerm.readBus(myBus)
                                
            returnedStatus = returnedBus.readBus()
            
            self.assertEquals(True, isinstance(returnedStatus, status.Status))
            self.assertEquals(remTermAddress, returnedStatus.address)
            self.assertEquals(False, returnedStatus.messageErrorFlag)
            self.assertEquals(False, returnedStatus.busyFlag)
            
            if (returnedStatus.serviceRequestFlag == True):
                probability_50_50_check_1 = True
                print "SERVICE REQUESTED!"
            else:
                probability_50_50_check_2 = True
                print "SERVICE NOT REQUESTED!"
        
        self.assertEquals(True, probability_50_50_check_1)
        self.assertEquals(True, probability_50_50_check_2)
        
    '''
        Test: Remote Terminal: Scenario 2: Instruct the remote terminal to receive data
    '''
    def test_003_002_readBus_scenario_2(self):
        
        # Create an instance of a Remote Terminal 
        remTermAddress = 5
        remTermSubAddress = 10
        myRemoteTerminal = remoteTerminal.RemoteTerminal(remTermAddress)
        
        # Set up a Command that instructs the remote terminal to receive 5 words of information
        wordCount = myRemoteTerminal.getAddress()
        myCommand = command.Command(myRemoteTerminal.getAddress())
        myCommand.setToCommandWord(remTermSubAddress)
        myCommand.setReceiveCommand()
        myCommand.setWordCount(wordCount)
        
        # Write myCommand to the Bus, as well as the number of data words to be received
        # Note these data values are for testing only. 
        myBus = bus.Bus()
        myBus.writeBus(myCommand)
        
        for index in range(wordCount):
            myBus.writeBus(data.Data(index))
            
        returnedBus = myRemoteTerminal.readBus(myBus)
        
        # myBus should now be empty
        self.assertEquals(0, myBus.busQueue.__len__())

        returnedStatus = returnedBus.readBus()
            
        # Returned Status should indicate All Systems Normal
        self.assertEquals(True, isinstance(returnedStatus, status.Status))
        self.assertEquals(remTermAddress, returnedStatus.address)
        self.assertEquals(False, returnedStatus.messageErrorFlag)
        self.assertEquals(False, returnedStatus.busyFlag)
        self.assertEquals(False, returnedStatus.serviceRequestFlag)

    '''
        Test: Remote Terminal: Scenario 3: Instruct the remote terminal to transmit data
    '''
    def test_003_003_readBus_scenario_3(self):
        
        # Create an instance of a Remote Terminal 
        remTermAddress = 8
        remTermSubAddress = 14
        myRemoteTerminal = remoteTerminal.RemoteTerminal(remTermAddress)
        
        # Set up a command that instructs the Remote Terminal to transmit 8 words of information 
        wordCount = myRemoteTerminal.getAddress()
        myCommand = command.Command(myRemoteTerminal.getAddress())
        myCommand.setToCommandWord()
        myCommand.setSubAddress(remTermSubAddress)
        myCommand.setTransmitCommand()
        myCommand.setWordCount(wordCount)
        
        # Write the command to the bus
        myBus = bus.Bus()
        myBus.writeBus(myCommand)
        
        # Inform the Remote Terminal that data is available on the bus
        returnedBus = myRemoteTerminal.readBus(myBus)
        
        # myBus should now be empty
        self.assertEquals(0, myBus.busQueue.__len__())
        
        # There should be 9 Words on the Returned bus (1 Status and 8 Data).
        self.assertEquals(wordCount + 1, returnedBus.busQueue.__len__())
        
        returnedStatus = returnedBus.readBus()
        
        # Returned Status should indicate All Systems Normal
        self.assertEquals(True, isinstance(returnedStatus, status.Status))
        self.assertEquals(remTermAddress, returnedStatus.address)
        self.assertEquals(False, returnedStatus.messageErrorFlag)
        self.assertEquals(False, returnedStatus.busyFlag)
        self.assertEquals(False, returnedStatus.serviceRequestFlag)
        
        # There should now be 8 Data Words on the Returned bus.
        self.assertEquals(wordCount, returnedBus.busQueue.__len__())
        
        for index in range(wordCount):
            transmitedDataWord = returnedBus.readBus()
            self.assertEquals(True, isinstance(transmitedDataWord, data.Data))
            print "Data Word Content:"
            print transmitedDataWord.getContent()
            # The Content should equal the index
            self.assertEquals(index, transmitedDataWord.getContent())
            
        # There should now be 0 Words on the Returned bus.
        self.assertEquals(0, returnedBus.busQueue.__len__())
        
    '''
        Test: Remote Terminal: Scenario 4: Receive a request from the remote 
              terminal to communicate with another remote terminal
    '''
    def test_003_004_readBus_scenario_4(self):
        
        # Because the Returned Command word can be 1 of 4 options, 
        # we run this test multiple times and make sure each occurrence is hit.
        probability_25_Percent_check_1 = False
        check_1_occurences = 0.0
        probability_25_Percent_check_2 = False
        check_2_occurences = 0.0
        probability_25_Percent_check_3 = False
        check_3_occurences = 0.0
        probability_25_Percent_check_4 = False
        check_4_occurences = 0.0
        
        runTests = 10000.0
        
        for testLoopIndex in range(0,  int(runTests)):
        
            # Create an instance of a Remote Termianl 
            rtAddress = 10
            rtSubAddress = 3
            myRemoteTerminal = remoteTerminal.RemoteTerminal(rtAddress)
            
            # Set up a command that requests status of the Remote Terminal
            myCommand = command.Command(myRemoteTerminal.getAddress())
            myCommand.setToModeCommand(command.Command.transmitStatusWord)
            
            # Write the word to the bus
            myBus = bus.Bus()
            myBus.writeBus(myCommand)
            
            # Inform the Remote Terminal that data is available on the bus
            returnedBus = myRemoteTerminal.readBus(myBus)
            
            # myBus should now be empty
            self.assertEquals(0, myBus.busQueue.__len__())
            
            # There should be 1 Word on the Returned bus
            self.assertEquals(1, returnedBus.busQueue.__len__())
            
            returnedStatus = returnedBus.readBus()
            
            # Returned Status is normal, other than the Service Request Flag could be set.
            # See Scenario 1 for through testing. 
            # I am assuming that the ModeCommand: 'transmitVectorWord' is what indicates that 
            #  the Remote Terminal wants to send a command to another Remote Terminal 
            
            self.assertEquals(True, isinstance(returnedStatus, status.Status))
            self.assertEquals(rtAddress, returnedStatus.address)
            self.assertEquals(False, returnedStatus.messageErrorFlag)
            self.assertEquals(False, returnedStatus.busyFlag)
            
            # Set up a Command that instructs the Remote Terminal to transmit a vector word
            mySecondCommand = command.Command(myRemoteTerminal.getAddress())
            mySecondCommand.setToModeCommand(command.Command.transmitVectorWord)
            
            # Write the Word to the Bus
            mySecondBus = bus.Bus()
            mySecondBus.writeBus(mySecondCommand)
            
            # Inform the Remote Terminal that data is available on the bus
            returnedBusTakeTwo = myRemoteTerminal.readBus(mySecondBus)
            
            # myBus should now be empty
            self.assertEquals(0, mySecondBus.busQueue.__len__())
            
            returnedStatusTakeTwo = returnedBusTakeTwo.readBus()
            
            # Returned Status should indicate All Systems Normal
            self.assertEquals(True, isinstance(returnedStatusTakeTwo, status.Status))
            self.assertEquals(rtAddress, returnedStatusTakeTwo.address)
            self.assertEquals(False, returnedStatusTakeTwo.messageErrorFlag)
            self.assertEquals(False, returnedStatusTakeTwo.busyFlag)
            self.assertEquals(False, returnedStatusTakeTwo.serviceRequestFlag)
            
            # The Returned Command Word has a 25% chance of being:
            # 1. ModeCommand: TRANSMIT_STATUS_WORD
            # 2. CommandWord: Set To Receive + Data
            # 3. CommandWord: Set To Transmit
            # 4. ModeCommand: TRANSMIT_VECTOR_WORD
            
            nextWordFromBus = returnedBusTakeTwo.readBus()
            
            if (isinstance(nextWordFromBus, command.Command)):
                # Check if both Mode Command Options were Hit
                if (nextWordFromBus.isModeCommand()):
                    if (nextWordFromBus.getModeCode() == command.Command.transmitStatusWord):
                        probability_25_Percent_check_1 = True
                        check_1_occurences = check_1_occurences + 1
                    elif (nextWordFromBus.getModeCode() == command.Command.transmitVectorWord):
                        probability_25_Percent_check_2 = True
                        check_2_occurences = check_2_occurences + 1
                # Check if both Command Word Options were Hit
                elif (not nextWordFromBus.isModeCommand()):
                    if (nextWordFromBus.isTransmitCommand()):
                        probability_25_Percent_check_3 = True
                        
                        # Check to make sure the random address is within the valid range of GT 0, LT 31
                        checkAddress = nextWordFromBus.getTerminalAddress()
                        checkAddressBool = False
                        
                        if (checkAddress < 31 and checkAddress > 0):
                            checkAddressBool = True
                        
                        self.assertEquals(checkAddressBool, True)
                        
                        check_3_occurences = check_3_occurences + 1
                        
                    elif (not nextWordFromBus.isTransmitCommand()):
                        probability_25_Percent_check_4 = True
                        check_4_occurences = check_4_occurences + 1
                        
                        for index in range(myRemoteTerminal.getAddress()):
                            transmitedDataWord = returnedBusTakeTwo.readBus()
                            self.assertEquals(True, isinstance(transmitedDataWord, data.Data))
                            print "Data Word Content:"
                            print transmitedDataWord.getContent()
                            # The Content should equal the index
                            self.assertEquals(index, transmitedDataWord.getContent())
                
            # There should now be 0 Words on the Returned bus.
            self.assertEquals(0, returnedBusTakeTwo.busQueue.__len__())
            
        self.assertEquals(True, probability_25_Percent_check_1)        
        self.assertAlmostEqual((float) (check_1_occurences / runTests), 0.25, None, None, 0.05)
        
        self.assertEquals(True, probability_25_Percent_check_2)
        self.assertAlmostEqual((float) (check_2_occurences / runTests), 0.25, None, None, 0.05)
        
        self.assertEquals(True, probability_25_Percent_check_3)
        self.assertAlmostEqual((float) (check_3_occurences / runTests), 0.25, None, None, 0.05)
        
        self.assertEquals(True, probability_25_Percent_check_4)
        self.assertAlmostEqual((float) (check_4_occurences / runTests), 0.25, None, None, 0.05)
        
        
        
        
        
        
        
