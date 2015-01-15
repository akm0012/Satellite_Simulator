'''
    Created on Apr 5, 2014
    Last updated on Apr 6, 2014

    The class RemoteTerminal represents a subsystem of one or more devices in a satellite.                

    @author: Andrew K. Marshall
    
    LOC: 95
'''
from CA04.prod import Bus as bus
from CA04.prod import Command as command
from CA04.prod import Status as status
from CA04.prod import Data as data

from random import randrange


class RemoteTerminal(object):

    '''
        Init a new RemoteTerminal
    '''
    def __init__(self, addressIn):
        
        # 1 <= (address must be) <= 30
        if (addressIn > 30 or addressIn < 1):
            raise ValueError("RemoteTerminal.__init__:  address must be in the range of 1-30")
        if (not isinstance(addressIn, int)):
            raise ValueError("RemoteTerminal.__init__:  address must be an integer")
        
        self.address = addressIn
        
    '''
        Returns the value of Address
    '''
    def getAddress(self):
        return self.address
    
    '''
        Notifies the remote terminal that something has been written 
        to the common bus connecting all remote terminals.
        
        Returns: An instance of Bus containing data produced by the remote terminal.
        
        Note: This method needs to be refactored heavily, however, since that was not part of
        this assignment's process I am going to delay in refactoring until later.
    '''
    def readBus(self, busIn):
        
        if (not isinstance(busIn, bus.Bus)):
            raise ValueError("RemoteTerminal.readBus:  bus must be a valid bus")
        
        # Covering Scenario 1
        incomingWord = busIn.readBus()
        
        if (isinstance(incomingWord, command.Command)):
#             print "Command Word In."
            
            if (incomingWord.getTerminalAddress() == self.address):
#                 print "Command Word Designated for this Remote terminal."
                
                if (incomingWord.isModeCommand()):
#                     print "Command is a ModeCommand."
                    
                    # Logic for Scenario 1
                    if (incomingWord.getModeCode() == command.Command.transmitStatusWord):
#                         print "Command is requesting Status of this Terminal."
                        
                        # We now create a Status Word with a 50/50 chance indicating this terminal needs service. 
                        returnedStatusWord = status.Status(self.address)
                        
                        randomInt = randrange(0, 101)
                        
                        # 50% Chance the Service Request Flag is Set
                        if (randomInt <= 100 and randomInt > 50):
#                             print "This Terminal Requires Service"
                            returnedStatusWord.setServiceRequest()
                            
                        returnBus = bus.Bus()
                        returnBus.writeBus(returnedStatusWord)
                        
                        return returnBus
                    
                    # Logic for Scenario 4
                    elif (incomingWord.getModeCode() == command.Command.transmitVectorWord):
#                         print "Command is requesting to Transmit Vector Word"
                        
                        # Create an All Systems Normal Status    
                        normalStatus = status.Status(self.address)
                        
                        # Create a Bus that will be returned 
                        returnBus = bus.Bus()
                        
                        # Write the Status Word to the Bus
                        returnBus.writeBus(normalStatus)
                        
                        # Create a Command Word that would trigger any of these four 
                        # scenarios.
                        
                        # 1. ModeCommand: TRANSMIT_STATUS_WORD
                        # 2. CommandWord: Set To Receive + Data
                        # 3. CommandWord: Set To Transmit
                        # 4. ModeCommand: TRANSMIT_VECTOR_WORD
                        
                        randomInt = randrange(0, 101)
#                         print "RANDOM NUMBER IS:"
#                         print randomInt
                        
                        # 25% Chance it adds a ModeCommand: TRANSMIT_STATUS_WORD to the bus
                        if (randomInt >= 0 and randomInt < 25):
                            newModeCommand = command.Command(incomingWord.getTerminalAddress())
                            newModeCommand.setToModeCommand(command.Command.transmitStatusWord)
                            
                            returnBus.writeBus(newModeCommand)
                            
                        # 25% Chance it adds a Command Word: Set To Receive + Data Words
                        elif (randomInt >= 25 and randomInt < 50):
                            wordCount = incomingWord.getTerminalAddress()
                            newCommandWord_rx = command.Command(incomingWord.getTerminalAddress())
                            newCommandWord_rx.setToCommandWord()
                            newCommandWord_rx.setReceiveCommand()
                            newCommandWord_rx.setWordCount(wordCount)
                            
                            returnBus.writeBus(newCommandWord_rx)
                            
                            for index in range(wordCount):
                                returnBus.writeBus(data.Data(index))
                            
                        # 25% Chance it adds a Command Word: Set To Transmit
                        elif(randomInt >= 50 and randomInt < 75):
                            # Create a valid random terminal address to transmit to
                            randomTerminalAddress = randrange(1, 31)
#                             print "RANDOM Terminal IS:"
#                             print randomTerminalAddress
                            wordCount = randomTerminalAddress
                            newCommandWord_tx = command.Command(randomTerminalAddress)
                            newCommandWord_tx.setToCommandWord()
                            newCommandWord_tx.setTransmitCommand()
                            newCommandWord_tx.setWordCount(wordCount)
                            
                            returnBus.writeBus(newCommandWord_tx)
                        
                        # 25% Chance it adds a ModeCommand: TRANSMIT_VECTOR_WORD to the bus
                        elif(randomInt >= 75 and randomInt <= 100):
                            newModeCommand_vector = command.Command(incomingWord.getTerminalAddress())
                            newModeCommand_vector.setToModeCommand(command.Command.transmitVectorWord)
                            
                            returnBus.writeBus(newModeCommand_vector)
                            
                        else:
                            raise Exception("RemoteTerminal.readBus:  Random Number Not in Bounds.")
                            
                        return returnBus
                        
                    
                # Else Command is a Command Word    
                elif (not incomingWord.isModeCommand()):
                    print "Command is a Command Word"
                    
                    # Logic for Scenario 3
                    if (incomingWord.isTransmitCommand()):
#                         print "Command is instructing the Terminal to Transmit Data"
                        
                        # Create an All Systems Normal Status    
                        normalStatus = status.Status(self.address)
                        
                        # Create a Bus that will be returned 
                        returnBus = bus.Bus()
                        
                        # Write the Status Word to the Bus
                        returnBus.writeBus(normalStatus)
                        
                        txDataWordCount = incomingWord.getWordCount()
                        
                        for index in range(txDataWordCount):
#                             print "Adding Data Word with Value:"
#                             print index
                            dataToAdd = data.Data(index)
                            returnBus.writeBus(dataToAdd)
                            
                        return returnBus
                        
                    # Logic for Scenario 2    
                    elif (not incomingWord.isTransmitCommand()):
                        print "Command is instructing the Terminal to Receive Data"
                        
                        rxDataWordCount = incomingWord.getWordCount()
                        
                        for index in range(rxDataWordCount):
#                             print "Processing Data:"
                            dataValue = busIn.readBus().getContent()
#                             print dataValue
                            
                        # Create an All Systems Normal Status    
                        normalStatus = status.Status(self.address)
                        
                        # Create a Bus that will be returned 
                        returnBus = bus.Bus()
                        
                        # Write the Status Word to the Bus
                        returnBus.writeBus(normalStatus)
                        
                        return returnBus
                        
            















