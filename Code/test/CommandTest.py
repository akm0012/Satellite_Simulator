'''
    Created on Mar 31, 2014
    Last updated on Apr 6, 2014

    This is a test file used to test the Command Class

    @author: Andrew K. Marshall
'''
import unittest

import prod.Command as command

class commandTest(unittest.TestCase):

# Command
# Global Definitions: transmitStatusWord, shutDown, reset, transmitVectorWord, transmitLastCommand
# methods: instantiate, getTerminalAddress, setToCommandWord, setToModeCommand, getModeCode, isModeCommand,
#          setSubAddress, getSubAddress, setWordCount, getWordCount, setTransmitCommand, setReceiveCommand
#          isTransmitCommand, checkIfValidMode

# Global Definitions
    '''
        Test: Confirm Command.transmitStatusWord = 2
    '''
    def test100_010_GlobalDefinitions(self):
        
        theResult1 = 2
        
        self.assertEquals(theResult1, command.Command.transmitStatusWord)
        
    '''
        Test: Confirm Command.shutDown = 4
    '''
    def test100_020_GlobalDefinitions(self):
        
        theResult1 = 4
        
        self.assertEquals(theResult1, command.Command.shutDown)
        
    '''
        Test: Confirm Command.reset = 8
    '''
    def test100_030_GlobalDefinitions(self):
        
        theResult1 = 8
        
        self.assertEquals(theResult1, command.Command.reset)
        
    '''
        Test: Confirm Command.transmitVectorWord = 12
    '''
    def test100_040_GlobalDefinitions(self):
        
        theResult1 = 12
        
        self.assertEquals(theResult1, command.Command.transmitVectorWord)
        
    '''
        Test: Confirm Command.transmitLastCommand = 14
    '''
    def test100_050_GlobalDefinitions(self):
        
        theResult1 = 14
        
        self.assertEquals(theResult1, command.Command.transmitLastCommand)
        
    '''
        Test: Confirm Command.MODE_COMMAND = True
    '''
    def test100_060_GlobalDefinitions(self):
        
        theResult1 = True
        
        self.assertEquals(theResult1, command.Command.MODE_COMMAND)
        
    '''
        Test: Confirm Command.COMMAND_WORD = False
    '''
    def test100_070_GlobalDefinitions(self):
        
        theResult1 = False
        
        self.assertEquals(theResult1, command.Command.COMMAND_WORD)
        
    '''
        Test: Confirm Command.RECEIVE = True
    '''
    def test100_080_GlobalDefinitions(self):
        
        theResult1 = True
        
        self.assertEquals(theResult1, command.Command.RECEIVE)
        
    '''
        Test: Confirm Command.TRANSMIT = False
    '''
    def test100_090_GlobalDefinitions(self):
        
        theResult1 = False
        
        self.assertEquals(theResult1, command.Command.TRANSMIT)
        
# Constructor
    '''
        Test: Instantiate Command(1)
    '''
    def test200_010_InstantiateCommand(self):
        myCommand = command.Command(1)
        
        theResult1 = True
        theAddress = 1
        theCommandTypeFlag = command.Command.MODE_COMMAND
        theTransmitReceiveFlag = command.Command.RECEIVE
        theModeCommand = command.Command.transmitStatusWord
        
        self.assertEquals(theResult1, isinstance(myCommand, command.Command))
        self.assertEquals(theAddress, myCommand.address)
        self.assertEquals(theCommandTypeFlag, myCommand.commandTypeFlag)
        self.assertEquals(theTransmitReceiveFlag, myCommand.transmitReceiveFlag)
        self.assertEquals(theModeCommand, myCommand.modeCommand)
        
    '''
        Test: Instantiate Command(15)
    '''
    def test200_020_InstantiateCommand(self):
        myCommand = command.Command(15)
        
        theResult1 = True
        theAddress = 15
        theCommandTypeFlag = command.Command.MODE_COMMAND
        theTransmitReceiveFlag = command.Command.RECEIVE
        theModeCommand = command.Command.transmitStatusWord
        
        self.assertEquals(theResult1, isinstance(myCommand, command.Command))
        self.assertEquals(theAddress, myCommand.address)
        self.assertEquals(theCommandTypeFlag, myCommand.commandTypeFlag)
        self.assertEquals(theTransmitReceiveFlag, myCommand.transmitReceiveFlag)
        self.assertEquals(theModeCommand, myCommand.modeCommand)
        
    '''
        Test: Instantiate Command(30)
    '''
    def test200_030_InstantiateCommand(self):
        myCommand = command.Command(15)
        
        theResult1 = True
        theAddress = 15
        theCommandTypeFlag = command.Command.MODE_COMMAND
        theTransmitReceiveFlag = command.Command.RECEIVE
        theModeCommand = command.Command.transmitStatusWord
        
        self.assertEquals(theResult1, isinstance(myCommand, command.Command))
        self.assertEquals(theAddress, myCommand.address)
        self.assertEquals(theCommandTypeFlag, myCommand.commandTypeFlag)
        self.assertEquals(theTransmitReceiveFlag, myCommand.transmitReceiveFlag)
        self.assertEquals(theModeCommand, myCommand.modeCommand)
        
    '''
        Test: Instantiate Command(0)
    '''
    def test200_901_InstantiateCommand(self):
        self.assertRaises(ValueError, command.Command, 0)
        
    '''
        Test: Instantiate Command(31)
    '''
    def test200_902_InstantiateCommand(self):
        self.assertRaises(ValueError, command.Command, 31)
        
    '''
        Test: Instantiate Command('a')
    '''
    def test200_903_InstantiateCommand(self):
        self.assertRaises(ValueError, command.Command, 'a')
        
    '''
        Test: Instantiate Command('$')
    '''
    def test200_904_InstantiateCommand(self):
        self.assertRaises(ValueError, command.Command, '$')
        
# getTerminalAddress

    '''
        Test: Instantiate Command(1), call getTerminalAddress()
    '''
    def test300_001_getTerminalAddress(self):
        myCommand = command.Command(1)
        
        theResult1 = 1
        
        self.assertEquals(theResult1, myCommand.getTerminalAddress())
        
    '''
        Test: Instantiate Command(15), call getTerminalAddress()
    '''
    def test300_002_getTerminalAddress(self):
        myCommand = command.Command(15)
        
        theResult1 = 15
        
        self.assertEquals(theResult1, myCommand.getTerminalAddress())
        
    '''
        Test: Instantiate Command(30), call getTerminalAddress()
    '''
    def test300_003_getTerminalAddress(self):
        myCommand = command.Command(30)
        
        theResult1 = 30
        
        self.assertEquals(theResult1, myCommand.getTerminalAddress())
        
# setToCommandWord

    '''
        Test: Instantiate a valid Command. Call setToCommandWord()
    '''
    def test400_001_setToCommandWord(self):
        myCommand = command.Command(15)
        
        theResult1 = False
        theResult2 = command.Command.COMMAND_WORD
        theResult3 = 0
        theResult4 = 1
        
        self.assertEquals(theResult1, myCommand.setToCommandWord())
        self.assertEquals(theResult2, myCommand.commandTypeFlag)
        self.assertEquals(theResult3, myCommand.wordCount)
        self.assertEquals(theResult4, myCommand.subAddress)
        
    '''
        Test: Instantiate a valid Command. Call setToCommandWord() twice
    '''
    def test400_002_setToCommandWord(self):
        myCommand = command.Command(15)
        
        theResult1 = True
        theResult2 = command.Command.COMMAND_WORD
        theResult3 = 0
        theResult4 = 1
        
        myCommand.setToCommandWord()
        
        self.assertEquals(theResult1, myCommand.setToCommandWord())
        self.assertEquals(theResult2, myCommand.commandTypeFlag)
        self.assertEquals(theResult3, myCommand.wordCount)
        self.assertEquals(theResult4, myCommand.subAddress)
        
    '''
        Test: Instantiate a valid Command. Call setToCommandWord(1)
    '''
    def test400_003_setToCommandWord(self):
        myCommand = command.Command(15)
        
        theResult1 = False
        theResult2 = command.Command.COMMAND_WORD
        theResult3 = 0
        theResult4 = 1
                
        self.assertEquals(theResult1, myCommand.setToCommandWord(1))
        self.assertEquals(theResult2, myCommand.commandTypeFlag)
        self.assertEquals(theResult3, myCommand.wordCount)
        self.assertEquals(theResult4, myCommand.subAddress)
        
    '''
        Test: Instantiate a valid Command. Call setToCommandWord(30) twice
    '''
    def test400_004_setToCommandWord(self):
        myCommand = command.Command(15)
        
        theResult1 = True
        theResult2 = command.Command.COMMAND_WORD
        theResult3 = 0
        theResult4 = 30
        
        myCommand.setToCommandWord(30)
                
        self.assertEquals(theResult1, myCommand.setToCommandWord(30))
        self.assertEquals(theResult2, myCommand.commandTypeFlag)
        self.assertEquals(theResult3, myCommand.wordCount)
        self.assertEquals(theResult4, myCommand.subAddress)
        
    '''
        Test: Instantiate a valid Command. Call setToCommandWord(0)
    '''
    def test400_901_setToCommandWord(self):
        myCommand = command.Command(1)
        
        self.assertRaises(ValueError, myCommand.setToCommandWord, 0)
        
    '''
        Test: Instantiate a valid Command. Call setToCommandWord(31)
    '''
    def test400_902_setToCommandWord(self):
        myCommand = command.Command(1)
        
        self.assertRaises(ValueError, myCommand.setToCommandWord, 31)
        
    '''
        Test: Instantiate a valid Command. Call setToCommandWord('a')
    '''
    def test400_903_setToCommandWord(self):
        myCommand = command.Command(1)
        
        self.assertRaises(ValueError, myCommand.setToCommandWord, 'a')
        
    '''
        Test: Instantiate a valid Command. Call setToCommandWord('$')
    '''
    def test400_904_setToCommandWord(self):
        myCommand = command.Command(1)
        
        self.assertRaises(ValueError, myCommand.setToCommandWord, '$')

# checkIfValidMode

        '''
            Test: checkIfValidMode(transmitStatusWord)
        '''
        def test500_001_checkIfValidMode(self):
            self.assertEquals(True, command.Command.checkIfValidMode(self, command.Command.transmitStatusWord))
            
        '''
            Test: checkIfValidMode(SHUTDOWN)
        '''
        def test500_002_checkIfValidMode(self):
            self.assertEquals(True, command.Command.checkIfValidMode(self, command.Command.shutDown))
            
        '''
            Test: checkIfValidMode(RESET)
        '''
        def test500_003_checkIfValidMode(self):
            self.assertEquals(True, command.Command.checkIfValidMode(self, command.Command.reset))
        
        '''
            Test: checkIfValidMode(TRANSMIT_VECTOR_WORD)
        '''
        def test500_004_checkIfValidMode(self):
            self.assertEquals(True, command.Command.checkIfValidMode(self, command.Command.transmitVectorWord))
            
        '''
            Test: checkIfValidMode(transmitStatusWord)
        '''
        def test500_005_checkIfValidMode(self):
            self.assertEquals(True, command.Command.checkIfValidMode(self, command.Command.transmitLastCommand))
            
        '''
            Test: checkIfValidMode(1)
        '''
        def test500_901_checkIfValidMode(self):
            self.assertEquals(False, command.Command.checkIfValidMode(self, 1))
            
        '''
            Test: checkIfValidMode(13)
        '''
        def test500_902_checkIfValidMode(self):
            self.assertEquals(False, command.Command.checkIfValidMode(self, 13))
            
        '''
            Test: checkIfValidMode(100)
        '''
        def test500_903_checkIfValidMode(self):
            self.assertEquals(False, command.Command.checkIfValidMode(self, 100))
            
        '''
            Test: checkIfValidMode(5)
        '''
        def test500_904_checkIfValidMode(self):
            self.assertEquals(False, command.Command.checkIfValidMode(self, 5))
            
        '''
            Test: checkIfValidMode(-1)
        '''
        def test500_905_checkIfValidMode(self):
            self.assertEquals(False, command.Command.checkIfValidMode(self, -1))
            
        '''
            Test: checkIfValidMode('s')
        '''
        def test500_906_checkIfValidMode(self):
            self.assertRaises(ValueError, command.Command.checkIfValidMode, 's')
            
        '''
            Test: checkIfValidMode('#')
        '''
        def test500_907_checkIfValidMode(self):
            self.assertRaises(ValueError, command.Command.checkIfValidMode, '#')
        
# setToModeCommand
        
    '''
        Test: Instantiate a valid Command. Call setToCommandWord(), then call setToModeCommand()
    '''
    def test600_001_setToModeCommand(self):
        myCommand = command.Command(15)
        
        theResult1 = command.Command.transmitStatusWord
        theResult2 = command.Command.MODE_COMMAND
        theResult3 = 0
        
        myCommand.setToCommandWord()
        
        self.assertEquals(theResult1, myCommand.setToModeCommand())
        self.assertEquals(theResult2, myCommand.commandTypeFlag)
        self.assertEquals(theResult3, myCommand.subAddress)
        
    '''
        Test: Instantiate a valid Command. Call setToCommandWord(), then call setToModeCommand(transmitStatusWord)
    '''
    def test600_002_setToModeCommand(self):
        myCommand = command.Command(15)
        
        theResult1 = command.Command.transmitStatusWord
        theResult2 = command.Command.MODE_COMMAND
        theResult3 = 0
        
        myCommand.setToCommandWord()
        
        self.assertEquals(theResult1, myCommand.setToModeCommand(command.Command.transmitStatusWord))
        self.assertEquals(theResult2, myCommand.commandTypeFlag)
        self.assertEquals(theResult3, myCommand.subAddress)
        
    '''
        Test: Instantiate a valid Command. Call setToCommandWord(), then call setToModeCommand(shutDown)
    '''
    def test600_003_setToModeCommand(self):
        myCommand = command.Command(15)
        
        theResult1 = command.Command.shutDown
        theResult2 = command.Command.MODE_COMMAND
        theResult3 = 0
        
        myCommand.setToCommandWord()
        
        self.assertEquals(theResult1, myCommand.setToModeCommand(command.Command.shutDown))
        self.assertEquals(theResult2, myCommand.commandTypeFlag)
        self.assertEquals(theResult3, myCommand.subAddress)
        
    '''
        Test: Instantiate a valid Command. Call setToCommandWord(), then call setToModeCommand(reset)
    '''
    def test600_004_setToModeCommand(self):
        myCommand = command.Command(15)
        
        theResult1 = command.Command.reset
        theResult2 = command.Command.MODE_COMMAND
        theResult3 = 0
        
        myCommand.setToCommandWord()
        
        self.assertEquals(theResult1, myCommand.setToModeCommand(command.Command.reset))
        self.assertEquals(theResult2, myCommand.commandTypeFlag)
        self.assertEquals(theResult3, myCommand.subAddress)
        
    '''
        Test: Instantiate a valid Command. Call setToCommandWord(), then call setToModeCommand(transmitVectorWord)
    '''
    def test600_005_setToModeCommand(self):
        myCommand = command.Command(15)
        
        theResult1 = command.Command.transmitVectorWord
        theResult2 = command.Command.MODE_COMMAND
        theResult3 = 0
        
        myCommand.setToCommandWord()
        
        self.assertEquals(theResult1, myCommand.setToModeCommand(command.Command.transmitVectorWord))
        self.assertEquals(theResult2, myCommand.commandTypeFlag)
        self.assertEquals(theResult3, myCommand.subAddress)
        
    '''
        Test: Instantiate a valid Command. Call setToCommandWord(), then call setToModeCommand(transmitLastCommand)
    '''
    def test600_006_setToModeCommand(self):
        myCommand = command.Command(15)
        
        theResult1 = command.Command.transmitLastCommand
        theResult2 = command.Command.MODE_COMMAND
        theResult3 = 0
        
        myCommand.setToCommandWord()
        
        self.assertEquals(theResult1, myCommand.setToModeCommand(command.Command.transmitLastCommand))
        self.assertEquals(theResult2, myCommand.commandTypeFlag)
        self.assertEquals(theResult3, myCommand.subAddress)
        
    '''
        Test: Instantiate a valid Command. Call setToCommandWord(), then call setToModeCommand(55)
    '''
    def test600_901_setToModeCommand(self):
        myCommand = command.Command(15)
        
        myCommand.setToCommandWord()
        
        self.assertRaises(ValueError, myCommand.setToModeCommand, 55)
        
    '''
        Test: Instantiate a valid Command. Call setToCommandWord(), then call setToModeCommand(1)
    '''
    def test600_902_setToModeCommand(self):
        myCommand = command.Command(15)
        
        myCommand.setToCommandWord()
        
        self.assertRaises(ValueError, myCommand.setToModeCommand, 1)
        
    '''
        Test: Instantiate a valid Command. Call setToCommandWord(), then call setToModeCommand('a')
    '''
    def test600_903_setToModeCommand(self):
        myCommand = command.Command(15)
        
        myCommand.setToCommandWord()
        
        self.assertRaises(ValueError, myCommand.setToModeCommand, 'a')
        
    '''
        Test: Instantiate a valid Command. Call setToCommandWord(), then call setToModeCommand('$')
    '''
    def test600_904_setToModeCommand(self):
        myCommand = command.Command(15)
        
        myCommand.setToCommandWord()
        
        self.assertRaises(ValueError, myCommand.setToModeCommand, '$')

# getModeCode()

    '''
        Test: Instantiate a valid Command. Call setToCommandWord().  Call getModeCode()
    '''
    def test700_901_getModeCode(self):
        myCommand = command.Command(1)
        
        myCommand.setToCommandWord()
        
        self.assertRaises(ValueError, myCommand.getModeCode)
        
    '''
        Test: Instantiate a valid Command.  Call getModeCode()
    '''
    def test700_001_getModeCode(self):
        myCommand = command.Command(1)
        
        theResult1 = command.Command.transmitStatusWord
        
        self.assertEquals(theResult1, myCommand.getModeCode())
        
    '''
        Test: Instantiate a valid Command.Call setToModeCommand(shutDown). Call getModeCode()
    '''
    def test700_002_getModeCode(self):
        myCommand = command.Command(1)
        
        myCommand.setToModeCommand(command.Command.shutDown)
        
        theResult1 = command.Command.shutDown
        
        self.assertEquals(theResult1, myCommand.getModeCode())
        
    '''
        Test: Instantiate a valid Command.Call setToModeCommand(reset). Call getModeCode()
    '''
    def test700_003_getModeCode(self):
        myCommand = command.Command(1)
        
        myCommand.setToModeCommand(command.Command.reset)
        
        theResult1 = command.Command.reset
        
        self.assertEquals(theResult1, myCommand.getModeCode())
        
    '''
        Test: Instantiate a valid Command.Call setToModeCommand(transmitVectorWord). Call getModeCode()
    '''
    def test700_004_getModeCode(self):
        myCommand = command.Command(1)
        
        myCommand.setToModeCommand(command.Command.transmitVectorWord)
        
        theResult1 = command.Command.transmitVectorWord
        
        self.assertEquals(theResult1, myCommand.getModeCode())
        
    '''
        Test: Instantiate a valid Command.Call setToModeCommand(transmitLastCommand). Call getModeCode()
    '''
    def test700_005_getModeCode(self):
        myCommand = command.Command(1)
        
        myCommand.setToModeCommand(command.Command.transmitLastCommand)
        
        theResult1 = command.Command.transmitLastCommand
        
        self.assertEquals(theResult1, myCommand.getModeCode())
        
# isModeCommand()

    '''
        Test: Instantiate a valid Command.  Call isModeCommand()
    '''
    def test800_001_isModeCommand(self):
        myCommand = command.Command(1)
        
        theResult1 = True
        
        self.assertEquals(theResult1, myCommand.isModeCommand())
        
    '''
        Test: Instantiate a valid Command.  Call setToCommandWord(). Call isModeCommand()
    '''
    def test800_002_isModeCommand(self):
        myCommand = command.Command(1)
        
        theResult1 = False
        
        myCommand.setToCommandWord()
        
        self.assertEquals(theResult1, myCommand.isModeCommand())
        
    '''
        Test: Instantiate a valid Command.  Call setToCommandWord(). Call isModeCommand()
    '''
    def test800_003_isModeCommand(self):
        myCommand = command.Command(1)
        
        theResult1 = True
        
        myCommand.setToCommandWord()
        myCommand.setToModeCommand(command.Command.reset)
        
        self.assertEquals(theResult1, myCommand.isModeCommand())
        
# setSubAddress

    '''
        Test: Instantiate a valid Command. Call setSubAddress(5)
    '''
    def test900_901_setSubAddress(self):
        myCommand = command.Command(1)
        
        self.assertRaises(ValueError, myCommand.setSubAddress, 5)
        
    '''
        Test: Instantiate a valid Command. Switch from Mode -> Command Word -> Mode. Call setSubAddress(5)
    '''
    def test900_902_setSubAddress(self):
        myCommand = command.Command(1)
        
        myCommand.setToCommandWord()
        
        myCommand.setToModeCommand()
        
        self.assertRaises(ValueError, myCommand.setSubAddress, 5)
        
    '''
        Test: Instantiate a valid Command. Call setToCommandWord(). Call setSubAddress(1)
    '''
    def test900_001_setSubAddress(self):
        myCommand = command.Command(1)
        
        myCommand.setToCommandWord()
        
        theResult1 = 1
        
        self.assertEquals(theResult1, myCommand.setSubAddress(1))
        self.assertEquals(theResult1, myCommand.subAddress)
        
    '''
        Test: Instantiate a valid Command. Call setToCommandWord(). Call setSubAddress(15)
    '''
    def test900_002_setSubAddress(self):
        myCommand = command.Command(1)
        
        myCommand.setToCommandWord()
        
        theResult1 = 15
        
        self.assertEquals(theResult1, myCommand.setSubAddress(15))
        self.assertEquals(theResult1, myCommand.subAddress)
        
    '''
        Test: Instantiate a valid Command. Call setToCommandWord(). Call setSubAddress(30)
    '''
    def test900_003_setSubAddress(self):
        myCommand = command.Command(1)
        
        myCommand.setToCommandWord()
        
        theResult1 = 30
        
        self.assertEquals(theResult1, myCommand.setSubAddress(30))
        self.assertEquals(theResult1, myCommand.subAddress)
     
    '''
        Test: Instantiate a valid Command. Call setToCommandWord(). Call setSubAddress(0)
    '''
    def test900_903_setSubAddress(self):
        myCommand = command.Command(1)
        
        myCommand.setToCommandWord()
                
        self.assertRaises(ValueError, myCommand.setSubAddress, 0)
        
    '''
        Test: Instantiate a valid Command. Call setToCommandWord(). Call setSubAddress(31)
    '''
    def test900_904_setSubAddress(self):
        myCommand = command.Command(1)
        
        myCommand.setToCommandWord()
                
        self.assertRaises(ValueError, myCommand.setSubAddress, 31)
        
    '''
        Test: Instantiate a valid Command. Call setToCommandWord(). Call setSubAddress('a')
    '''
    def test900_905_setSubAddress(self):
        myCommand = command.Command(1)
        
        myCommand.setToCommandWord()
                
        self.assertRaises(ValueError, myCommand.setSubAddress, 'a')
        
    '''
        Test: Instantiate a valid Command. Call setToCommandWord(). Call setSubAddress('$')
    '''
    def test900_906_setSubAddress(self):
        myCommand = command.Command(1)
        
        myCommand.setToCommandWord()
                
        self.assertRaises(ValueError, myCommand.setSubAddress, '$') 
        
    '''
        Test: Instantiate a valid Command. Call setToCommandWord(). 
        Call setToModeCommand(transmitLastCommand). Call setSubAddress(15)
    '''
    def test900_907_setSubAddress(self):
        myCommand = command.Command(1)
        
        myCommand.setToCommandWord()
        myCommand.setToModeCommand(command.Command.transmitLastCommand)
                
        self.assertRaises(ValueError, myCommand.setSubAddress, 15)  
        
# getSubAddress

    '''
        Test: Instantiate a valid Command. Call setToCommandWord(). Call setSubAddress(1). Call getSubAddress().
    '''
    def test110_001_getSubAddress(self):
        myCommand = command.Command(1)
        
        theResult = 1

        myCommand.setToCommandWord()
        myCommand.setSubAddress(1)
        
        self.assertEquals(theResult, myCommand.getSubAddress())
        
    '''
        Test: Instantiate a valid Command. Call setToCommandWord(). Call setSubAddress(15). Call getSubAddress().
    '''
    def test110_002_getSubAddress(self):
        myCommand = command.Command(1)
        
        theResult = 15

        myCommand.setToCommandWord()
        myCommand.setSubAddress(15)
        
        self.assertEquals(theResult, myCommand.getSubAddress())
        
    '''
        Test: Instantiate a valid Command. Call setToCommandWord(). Call setSubAddress(30). Call getSubAddress().
    '''
    def test110_003_getSubAddress(self):
        myCommand = command.Command(1)
        
        theResult = 30

        myCommand.setToCommandWord()
        myCommand.setSubAddress(30)
        
        self.assertEquals(theResult, myCommand.getSubAddress())
        
    '''
        Test: Instantiate a valid Command. Call getSubAddress().
    '''
    def test110_901_getSubAddress(self):
        myCommand = command.Command(1)
                        
        self.assertRaises(ValueError, myCommand.getSubAddress)
        
    '''
        Test: Instantiate a valid Command. Call setToModeCommand(transmitVectorWord). Call getSubAddress().
    '''
    def test110_902_getSubAddress(self):
        myCommand = command.Command(1)
        
        myCommand.setToModeCommand(command.Command.transmitVectorWord)
                        
        self.assertRaises(ValueError, myCommand.getSubAddress)
        
# setWordCount

    '''
        Test: Instantiate a valid Command. Call setWordCount(5)
    '''
    def test_120_901_setWordCount(self):
        myCommand = command.Command(1)
        
        self.assertRaises(ValueError, myCommand.setWordCount, 5)
        
    '''
        Test: Instantiate a valid Command. Call setToModeCommand(transmitVectorWord). Call setWordCount(5)
    '''
    def test_120_902_setWordCount(self):
        myCommand = command.Command(1)
        
        myCommand.setToModeCommand(command.Command.transmitVectorWord)
        
        self.assertRaises(ValueError, myCommand.setWordCount, 5)
        
    '''
        Test: Instantiate a valid Command. Call setToCommandWord(15). Call setWordCount(1)
    '''
    def test_120_001_setWordCount(self):
        myCommand = command.Command(1)
        
        myCommand.setToCommandWord(15)
        
        theResult = 1
        
        self.assertEquals(theResult, myCommand.setWordCount(1))
        self.assertEquals(theResult, myCommand.wordCount)
        
    '''
        Test: Instantiate a valid Command. Call setToCommandWord(). Call setWordCount(15)
    '''
    def test_120_002_setWordCount(self):
        myCommand = command.Command(1)
        
        myCommand.setToCommandWord()
        
        theResult = 15
        
        self.assertEquals(theResult, myCommand.setWordCount(15))
        self.assertEquals(theResult, myCommand.wordCount)
        
    '''
        Test: Instantiate a valid Command. Call setToCommandWord(). Call setWordCount(31)
    '''
    def test_120_003_setWordCount(self):
        myCommand = command.Command(1)
        
        myCommand.setToCommandWord()
        
        theResult = 31
        
        self.assertEquals(theResult, myCommand.setWordCount(31))
        self.assertEquals(theResult, myCommand.wordCount)
        
    '''
        Test: Instantiate a valid Command. Call setToCommandWord(). Call setWordCount(0)
    '''
    def test_120_903_setWordCount(self):
        myCommand = command.Command(1)
        
        myCommand.setToCommandWord()
                
        self.assertRaises(ValueError, myCommand.setWordCount, 0)
        
    '''
        Test: Instantiate a valid Command. Call setToCommandWord(). Call setWordCount(32)
    '''
    def test_120_904_setWordCount(self):
        myCommand = command.Command(1)
        
        myCommand.setToCommandWord()
                
        self.assertRaises(ValueError, myCommand.setWordCount, 32)
        
    '''
        Test: Instantiate a valid Command. Call setToCommandWord(). Call setWordCount('a')
    '''
    def test_120_905_setWordCount(self):
        myCommand = command.Command(1)
        
        myCommand.setToCommandWord()
                
        self.assertRaises(ValueError, myCommand.setWordCount, 'a')
        
    '''
        Test: Instantiate a valid Command. Call setToCommandWord(). Call setWordCount('%')
    '''
    def test_120_906_setWordCount(self):
        myCommand = command.Command(1)
        
        myCommand.setToCommandWord()
                
        self.assertRaises(ValueError, myCommand.setWordCount, '%')
        
# getWordCount

    '''
        Test: Instantiate a valid Command. Call setToCommandWord(). Call getWordCount()
    '''
    def test_130_001_getWordCount(self):
        myCommand = command.Command(1)
        
        myCommand.setToCommandWord()
        
        theResult = 0
        
        self.assertEquals(theResult, myCommand.getWordCount())
        
    '''
        Test: Instantiate a valid Command. Call setToCommandWord(). Call setWordCount(1). Call getWordCount()
    '''
    def test_130_002_getWordCount(self):
        myCommand = command.Command(1)
        
        myCommand.setToCommandWord()
        
        myCommand.setWordCount(1)
        
        theResult = 1
        
        self.assertEquals(theResult, myCommand.getWordCount())
        
    '''
        Test: Instantiate a valid Command. Call setToCommandWord(). Call setWordCount(15). Call getWordCount()
    '''
    def test_130_003_getWordCount(self):
        myCommand = command.Command(1)
        
        myCommand.setToCommandWord()
        
        myCommand.setWordCount(15)
        
        theResult = 15
        
        self.assertEquals(theResult, myCommand.getWordCount())
        
    '''
        Test: Instantiate a valid Command. Call setToCommandWord(). Call setWordCount(32). Call getWordCount()
    '''
    def test_130_004_getWordCount(self):
        myCommand = command.Command(1)
        
        myCommand.setToCommandWord()
        
        myCommand.setWordCount(31)
        
        theResult = 31
        
        self.assertEquals(theResult, myCommand.getWordCount())
        
    '''
        Test: Instantiate a valid Command. Call setToModeCommand(transmitVectorWord). Call getWordCount()
    '''
    def test_130_901_getWordCount(self):
        myCommand = command.Command(1)
        
        myCommand.setToModeCommand(command.Command.transmitVectorWord)
        
        self.assertRaises(ValueError, myCommand.getWordCount)
        
    '''
        Test: Instantiate a valid Command. Call getWordCount()
    '''
    def test_130_902_getWordCount(self):
        myCommand = command.Command(1)
                
        self.assertRaises(ValueError, myCommand.getWordCount)
        
# setTransmitCommand

    '''
        Test: Instantiate a valid Command. Call setTransmitCommand()
    '''
    def test_140_001_setTransmitCommand(self):
        myCommand = command.Command(1)
        
        theResult1 = False
        theResult2 = command.Command.TRANSMIT
        
        self.assertEquals(theResult1, myCommand.setTransmitCommand())
        self.assertEquals(theResult2, myCommand.transmitReceiveFlag)
        
    '''
        Test: Instantiate a valid Command. Call setTransmitCommand(), twice.
    '''
    def test_140_002_setTransmitCommand(self):
        myCommand = command.Command(1)
        
        theResult1 = True
        theResult2 = command.Command.TRANSMIT
        
        myCommand.setTransmitCommand()
        
        self.assertEquals(theResult1, myCommand.setTransmitCommand())
        self.assertEquals(theResult2, myCommand.transmitReceiveFlag)

# setReceiveCommand

    '''
        Test: Instantiate a valid Command. Call setReceiveCommand()
    '''
    def test_150_001_setReceiveCommand(self):
        myCommand = command.Command(1)
        
        theResult1 = True
        theResult2 = command.Command.RECEIVE
        
        self.assertEquals(theResult1, myCommand.setReceiveCommand())
        self.assertEquals(theResult2, myCommand.transmitReceiveFlag)
        
    '''
        Test: Instantiate a valid Command. Call setTransmitCommand(), then call setReceiveCommand()
    '''
    def test_150_002_setReceiveCommand(self):
        myCommand = command.Command(1)
        
        theResult1 = False
        theResult2 = command.Command.RECEIVE
        
        myCommand.setTransmitCommand()
        
        self.assertEquals(theResult1, myCommand.setReceiveCommand())
        self.assertEquals(theResult2, myCommand.transmitReceiveFlag)

# isTransmitCommand

    '''
        Test: Instantiate a valid Command. Call isTransmitCommand()
    '''
    def test_160_001_isTransmitCommand(self):
        myCommand = command.Command(1)
        
        theResult1 = False
        
        self.assertEquals(theResult1, myCommand.isTransmitCommand())
        
    '''
        Test: Instantiate a valid Command. Call setTransmitCommand(). Call isTransmitCommand()
    '''
    def test_160_002_isTransmitCommand(self):
        myCommand = command.Command(1)
        
        theResult1 = True
        
        myCommand.setTransmitCommand()
        
        self.assertEquals(theResult1, myCommand.isTransmitCommand())
        
    '''
        Test: Instantiate a valid Command. Call setTransmitCommand(), then call setReceiveCommand(). Call isTransmitCommand()
    '''
    def test_160_003_isTransmitCommand(self):
        myCommand = command.Command(1)
        
        theResult1 = False
        
        myCommand.setTransmitCommand()
        myCommand.setReceiveCommand()
        
        self.assertEquals(theResult1, myCommand.isTransmitCommand())















        
        
