'''
    Created on Mar 31, 2014
    Last updated on Apr 6, 2014

    The class Command represents an instruction to be carried out by a remote terminal.                

    @author: Andrew K. Marshall
    
    LOC: 121
'''

class Command(object):
    
    # Global Definitions
    # Mode Code Constants
    transmitStatusWord = 2
    shutDown = 4
    reset = 8
    transmitVectorWord = 12
    transmitLastCommand = 14
    
    # Used to set Command Type Flag
    MODE_COMMAND = True
    COMMAND_WORD = False
    
    # Used to set the Transmit / Receive Flag
    RECEIVE = True
    TRANSMIT = False
    

    '''
        Inits a new Command.
    '''
    def __init__(self, addressIn):
        
        # 1 <= (address must be) <= 30
        if (addressIn > 30 or addressIn < 1):
            raise ValueError("Command.__init__:  address must be in the range of 1-30")
        
        if (not isinstance(addressIn, int)):
            raise ValueError("Command.__init__:  address must be an integer")
        
        self.address = addressIn
        self.commandTypeFlag = Command.MODE_COMMAND
        self.transmitReceiveFlag = Command.RECEIVE
        self.modeCommand = Command.transmitStatusWord
        self.wordCount = None
        self.subAddress = None
        
    '''
        Returns the Terminal Address
    '''
    def getTerminalAddress(self):
        return self.address
    
    '''
        Sets the Command Type to Command Word with a specific sub address. 
        Returns True if Command was previously set as a Command Word. 
        Returns False if Command was set to a Mode Command.
        
        If no address is specified it will default to 1.
    '''
    def setToCommandWord(self, subAddressIn=None):
        
        # If parameter is missing 
        if (subAddressIn == None):
            self.subAddress = 1
            
        # 1 <= (address must be) <= 30
        elif (subAddressIn > 30 or subAddressIn < 1):
            raise ValueError("Command.setToCommandWord:  address must be in the range of 1-30")
        
        elif (not isinstance(subAddressIn, int)):
            raise ValueError("Command.setToCommandWord:  address must be an integer")
            
        if (self.commandTypeFlag == Command.COMMAND_WORD):
            tempReturn = True
        else:
            tempReturn = False
        
        self.commandTypeFlag = Command.COMMAND_WORD
        self.wordCount = 0
        
        if(subAddressIn != None):
            self.subAddress = subAddressIn
        
        return tempReturn
        
    '''
        Sets the Command Type to Mode Command. Returns True if Command was
        previously set as a Command Word. Returns False if Command was set
        to a Mode Command.
    '''
    def setToModeCommand(self, modeIn=None):
        
        # If parameter is missing
        if (modeIn == None):
            self.commandTypeFlag = Command.MODE_COMMAND
            self.modeCommand = Command.transmitStatusWord
            self.subAddress = 0
            return self.modeCommand
        
        elif (not isinstance(modeIn, int)):
            raise ValueError("Command.setToModeCommand:  modeToCheck must be an integer")
        
        elif(not self.checkIfValidMode(modeIn)):
            raise ValueError("Command.setToModeCommand:  mode must be a valid Mode")
        
        # If parameter is not missing, and is valid
        self.commandTypeFlag = Command.MODE_COMMAND
        self.modeCommand = modeIn
        self.subAddress = 0
        
        return self.modeCommand
        
    '''
        Helper function that checks to see if a mode if a valid Mode Command. 
        
        Returns True if modeToCheck is a valid Mode.  
        Returns False if it is not a valid Mode. 
    '''
    def checkIfValidMode(self, modeToCheck):
        
        if (not isinstance(modeToCheck, int)):
            raise ValueError("Command.checkIfValidMode:  modeToCheck must be an integer")

        if(modeToCheck == Command.transmitStatusWord or
        modeToCheck == Command.shutDown or
        modeToCheck == Command.reset or
        modeToCheck == Command.transmitVectorWord or
        modeToCheck == Command.transmitLastCommand):
            return True
        
        else:
            return False
        
    '''
        Returns the Mode Code associated with the instance. 
    
        Throws a Value Error if it is called on a non- Mode Command.
    '''
    def getModeCode(self):
        
        if (self.commandTypeFlag != Command.MODE_COMMAND):
            raise ValueError("Command.getModeCode:  must be called on a Mode Command.")
        
        return self.modeCommand
    
    '''
        Returns True if the instance is a Mode Command.
        Returns False if the instance is a Command Word.
    '''
    def isModeCommand(self):
        
        if(self.commandTypeFlag == Command.MODE_COMMAND):
            return True
        
        elif(self.commandTypeFlag == Command.COMMAND_WORD):
            return False
        
        else:
            raise ValueError("Command.isModeCommand:  ERROR! Command is not set to either Mode Command or Command Word.")

    '''
        Sets the Sub Address. Returns the sub address that was just set. 
    '''
    def setSubAddress(self, addressIn):
        
        # 1 <= (address must be) <= 30
        if (addressIn > 30 or addressIn < 1):
            raise ValueError("Command.setSubAddress:  address must be in the range of 1-30")
        
        elif (not isinstance(addressIn, int)):
            raise ValueError("Command.setSubAddress:  address must be an integer")
        
        elif (self.commandTypeFlag != Command.COMMAND_WORD):
            raise ValueError("Command.setSubAddress:  must be called on a Command Word")
        
        self.subAddress = addressIn
        return self.subAddress

    '''
        Returns the Sub Address.  Throws an exception if you call this on a Mode Command.
    '''
    def getSubAddress(self):
        
        if (self.commandTypeFlag != Command.COMMAND_WORD):
            raise ValueError("Command.getSubAddress:  must be called on a Command Word")
        
        return self.subAddress

    '''
        Sets the word count.  Word count must be in range of 1-31        
        
        Can only be called on a Command Word.
        
        Throws exception if called on a Mode Command, or if not in range.
    '''
    def setWordCount(self, wordCountIn):
        
        # 1 <= (wordCountIn must be) <= 31
        if (wordCountIn > 31 or wordCountIn < 1):
            raise ValueError("Command.setWordCount:  address must be in the range of 1-31")
        
        elif (not isinstance(wordCountIn, int)):
            raise ValueError("Command.setWordCount:  address must be an integer")
        
        elif (self.commandTypeFlag != Command.COMMAND_WORD):
            raise ValueError("Command.setWordCount:  must be called on a Command Word")
        
        self.wordCount = wordCountIn
        
        return self.wordCount
    
    '''
        Returns the Word Count. 
        
        Must be called on a Command Word or will raise an exception. 
    '''
    def getWordCount(self):
        
        if (self.commandTypeFlag != Command.COMMAND_WORD):
            raise ValueError("Command.getWordCount:  must be called on a Command Word")

        return self.wordCount
    
    '''
        Sets the transmitReceiveFlag to transmit.  Returns True if the instance was 
        previously set to transmit.  Otherwise it returns false. 
    '''
    def setTransmitCommand(self):
        
        if (self.transmitReceiveFlag == Command.TRANSMIT):
            returnTemp = True
        else:
            returnTemp = False
        
        self.transmitReceiveFlag = Command.TRANSMIT
        return returnTemp

    '''
        Sets the transmitReceiveFlag to receive.  Returns True if the instance was 
        previously set to receive.  Otherwise it returns false. 
    '''
    def setReceiveCommand(self):
        
        if (self.transmitReceiveFlag == Command.RECEIVE):
            returnTemp = True
        else:
            returnTemp = False
        
        self.transmitReceiveFlag = Command.RECEIVE
        return returnTemp
    
    '''
        Returns True if the Transmit Flag is set. Otherwsie returns False
    '''
    def isTransmitCommand(self):
        
        if (self.transmitReceiveFlag == Command.TRANSMIT):
            return True
        elif (self.transmitReceiveFlag == Command.RECEIVE):
            return False
        else:
            raise StandardError("Command.isTransmitCommand:  Transmit/Receive Flag has serious issues")









        
        
