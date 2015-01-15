'''
    Created on Apr 19, 2014
    Last updated on Apr 20, 2014

    The class BusController represents the on board master control 
    computer that controls communication with, and among, remote terminals.                                

    @author: Andrew K. Marshall
    
    LOC: 113
'''

import CA04.prod.Command as Command
import CA04.prod.Bus as Bus

class BusController(object):
    
    '''
        Init a new BusController
    '''
    def __init__(self):
        self.pollFrame = []
        self.linkedSatellite = None
        self.wordsWrittenToBus = 0
        
        # Used for testing purposes
        self.test_status_normal = 0
        self.test_status_service = 0
        
        self.test_vector_status = 0
        self.test_vector_receive = 0
        self.test_vector_transmit = 0
        self.test_vector_vector = 0
        
    '''
        Sets the Poll Frame. Identifies the order in which to poll the remote terminals
    '''
    def setPollFrame(self, rtList=[]):
        
        rtListCheck = self.isValidRemoteTerminalList(rtList)
        
        if (rtListCheck == False):
            raise ValueError("BusController.setPollFrame:  rtList but be in range 1 - 30.")

        if (self.linkedSatellite == None):
            raise ValueError("BusController.setPollFrame:  No Satellite has been linked.")

        satelliteAddressCheck = self.isValidAddressOnSatellite(rtList)
        
        if (satelliteAddressCheck == False):
            raise ValueError("BusController.setPollFrame:  There is an invalid Remote Terminal in the List.")
        
        self.pollFrame = rtList
        
        return rtList.__len__()
        
    '''
        Checks to make sure the list of remote terminals are installed in the satellite.
    '''
    def isValidAddressOnSatellite(self, rtList=[]):
        
        if (rtList == []):
            return True
        else:
            
            addressList = self.linkedSatellite.getRemoteTerminalAddresses()
            
            for loopIndex in range(0, rtList.__len__()):
                if (addressList.count(rtList[loopIndex]) == 0):
                    return False
                
        
        
    '''
        Links a Satellite with the Bus Controller
    '''
    def linkWithSatellite(self, satelliteIn):
        
        # Needed to put import here to avoid a circular import reference
        import CA05.prod.Satellite as Sat
        
        if (not isinstance(satelliteIn, Sat.Satellite)):
            raise ValueError("BusController.linkWithSatellite:  Parameter must be a valid Satellite.")
        
        self.linkedSatellite = satelliteIn
        
    '''
        Determines if a List has valid Remote Terminal Address in it.
    '''
    def isValidRemoteTerminalList(self, rtList=[]):
        
        if (rtList == []):
            return True
        
        if (not isinstance(rtList, list)):
            return False
        
        else:
            
            for loopIndex in range(0, rtList.__len__()):
                if (rtList[loopIndex] < 1 or rtList[loopIndex] > 30):
                    return False
                if (not isinstance(rtList[loopIndex], int)):
                    return False
        
        return True
    
    '''
        Returns the number of unique address in the list.
        
        Assumes all input has already been validated. 
    '''
    def countUniqueAddresses(self, rtList=[]):
        
        if (rtList == []):
            return 0
        
        else:
            
            countingList = []
            count = 0
            
            # Iterate over the sorted list
            for loopIndex in range(0, rtList.__len__()):
                
                if (countingList.count(rtList[loopIndex]) == 0):
                    
                    countingList.append(rtList[loopIndex])
                    count = count + 1
            
            return count
        
        
    '''
        Notifies the bus controller that it should iterate through the poll frame once, 
        polling each remote terminal for status and taking action if the remote terminal 
        requests service.  If the poll frame is empty, the remote terminals are polled by 
        address in ascending order.  No action is taken if no remote terminal has been 
        added to the satellite.                
    '''
    def poll(self):
        
        remoteTerminalList = self.linkedSatellite.getRemoteTerminals()
        
        terminalPollCount = 0
        
        # If the poll frame is empty we poll by the terminal addresses in ascending order 
        if (self.pollFrame == []):
            # Set the poll frame to the address list, then sort.
            self.pollFrame = self.linkedSatellite.getRemoteTerminalAddresses()
            self.pollFrame.sort()
            
        for pollIndex in range(0, self.pollFrame.__len__()):
            
            for rtAddressIndex in range(0, remoteTerminalList.__len__()):
                
                if (self.pollFrame[pollIndex] == remoteTerminalList[rtAddressIndex].getAddress()):
                    
                    terminalPollCount = self.performStatusCheck(remoteTerminalList, terminalPollCount, rtAddressIndex)
                    
                    break
                
        return terminalPollCount


    '''
        Used to perform service on a remote terminal
    '''    
    def perfromServiceRoutine(self, remoteTerminalList, rtAddressIndex, myBus, returnedBus):
        
        print "BusController: Result of 1st Status Request: Service Requested"
    # Set up a Command that instructs the Remote Terminal to transmit a vector word
        myVectorCommand = Command.Command(remoteTerminalList[rtAddressIndex].getAddress())
        myVectorCommand.setToModeCommand(Command.Command.transmitVectorWord)
    
    # Write the Command to the Bus
        myBus = Bus.Bus()
        myBus.writeBus(myVectorCommand)
        self.incrementWordWrittenCount()
    
    # Read the returned bus and get the returned status word + additinal command.
        returnedBus = remoteTerminalList[rtAddressIndex].readBus(myBus)
        returnedStatus = returnedBus.readBus()
        self.incrementWordWrittenCount()
    
    # The Returned Command Word has a 25% chance of being:
    # 1. ModeCommand: TRANSMIT_STATUS_WORD
    # 2. CommandWord: Set To Receive + Data
    # 3. CommandWord: Set To Transmit
    # 4. ModeCommand: TRANSMIT_VECTOR_WORD
        
        returnedWordFromBus = returnedBus.readBus()
        if (isinstance(returnedWordFromBus, Command.Command)):
            # Check if both Mode Command Options were Hit
            
            if (returnedWordFromBus.isModeCommand()):
                if (returnedWordFromBus.getModeCode() == Command.Command.transmitStatusWord):
                    print "BusController: Result of Vector Word: Send Status"
                    self.incrementTestCounter("test_vector_status")
                
                elif (returnedWordFromBus.getModeCode() == Command.Command.transmitVectorWord):
                    print "BusController: Result of Vector Word: Send Vector Word"
                    self.incrementTestCounter("test_vector_vector")
            
            # Check if both Command Word Options were Hit
            elif (not returnedWordFromBus.isModeCommand()):
                if (returnedWordFromBus.isTransmitCommand()):
                    print "BusController: Result of Vector Word: Transmit Data"
                    self.incrementTestCounter("test_vector_transmit")
                
                elif (not returnedWordFromBus.isTransmitCommand()):
                    print "BusController: Result of Vector Word: Receive Data"
                    self.incrementTestCounter("test_vector_receive")
                    
                    for index in range(remoteTerminalList[rtAddressIndex].getAddress()):
                        transmitedDataWord = returnedBus.readBus()
                        self.incrementWordWrittenCount()
                        print "Data Word Content:"
                        print transmitedDataWord.getContent()
    
    # The Content should equal the index
    # There should now be 0 Words on the Returned bus.

    '''
        Clears the count of words that have been written to the bus. 
    '''
    def clearWordsWrittenToBus(self):
        self.wordsWrittenToBus = 0
        
    '''
        Returns the number of time the bus has been written to.
    '''
    def getWordsWrittenToBus(self):
        return self.wordsWrittenToBus
    
    '''
        Increments the count of words written to the bus
    '''
    def incrementWordWrittenCount(self):
        self.wordsWrittenToBus = self.wordsWrittenToBus + 1

    '''
        Performs a status check on a remote terminal, if the terminal requests service, 
        it will call "perform service routine."
    '''
    def performStatusCheck(self, remoteTerminalList, terminalPollCount, rtAddressIndex):
        
        print "Now Checking Remote Terminal: "
        print remoteTerminalList[rtAddressIndex].getAddress()
        
        # Set up the Command that will request status
        myStatusCommand = Command.Command(remoteTerminalList[rtAddressIndex].getAddress())
        myStatusCommand.setToModeCommand(Command.Command.transmitStatusWord)
        
        # Write the Command to the Bus
        myBus = Bus.Bus()
        myBus.writeBus(myStatusCommand)
        self.incrementWordWrittenCount()
        
        # Get the status word that was returned
        returnedBus = remoteTerminalList[rtAddressIndex].readBus(myBus)
        returnedStatus = returnedBus.readBus()
        
        if (returnedStatus.serviceRequestFlag == False):
            print "BusController: Result of 1st Status Request: All Systems Normal"
            self.incrementTestCounter("test_status_normal")
            
        # If the remote terminal requests service, we send it a vector word
        if (returnedStatus.serviceRequestFlag == True):
            self.incrementTestCounter("test_status_service")
            
            self.perfromServiceRoutine(remoteTerminalList, rtAddressIndex, myBus, returnedBus)
        
        terminalPollCount = terminalPollCount + 1
        
        return terminalPollCount

        

    '''
        Test: Used for testing the probability of scenarios
    '''
    def incrementTestCounter(self, counter):
        
        if (counter == "test_status_normal"):
            self.test_status_normal = self.test_status_normal + 1
        
        if (counter == "test_status_service"):
            self.test_status_service = self.test_status_service + 1
        
        if (counter == "test_vector_status"):
            self.test_vector_status = self.test_vector_status + 1
        
        if (counter == "test_vector_receive"):
            self.test_vector_receive = self.test_vector_receive + 1
            
        if (counter == "test_vector_transmit"):
            self.test_vector_transmit = self.test_vector_transmit + 1
            
        if (counter == "test_vector_vector"):
            self.test_vector_vector = self.test_vector_vector + 1
            
    '''
        Test: Used for testing the probability of scenarios
    '''
    def getTestCounter(self, counter):
        
        if (counter == "test_status_normal"):
            return self.test_status_normal
        
        if (counter == "test_status_service"):
            return self.test_status_service
        
        if (counter == "test_vector_status"):
            return self.test_vector_status
        
        if (counter == "test_vector_receive"):
            return self.test_vector_receive 
        
        if (counter == "test_vector_transmit"):
            return self.test_vector_transmit
            
        if (counter == "test_vector_vector"):
            return self.test_vector_vector
        
        if(counter == "all_vector_tests"):
            return self.test_vector_vector + self.test_vector_transmit + self.test_vector_receive + self.test_vector_status

        if(counter == "all_status_tests"):
            return self.test_status_normal + self.test_status_service




           
