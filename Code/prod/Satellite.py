'''
    Created on Apr 20, 2014
    Last updated on Apr 20, 2014
  
    The class Satellite represents the subsystems 
    that comprise the satellite.  It is an aggregation 
    of the bus controller, the bus, and the remote terminals.                                
  
    @author: Andrew K. Marshall
      
    LOC: 45
'''
import prod.RemoteTerminal as RemoteTerminal
import prod.BusController as BusController
  
  
class Satellite(object):
  
    '''
        Inits a new Satellite
    '''
    def __init__(self):
        self.subsystemsList = []
        self.subsystemsAddressList = []
        self.busController = None
          
    '''
        Adds a Remote Terminal to the Satellite. 
    '''
    def addRemoteTerminal(self, rt=None):
          
        if (rt == None):
            raise ValueError("Satellite.addRemoteTerminal:  Parameter must be a valid Remote Terminal.")
        if (not isinstance(rt, RemoteTerminal.RemoteTerminal)):
            raise ValueError("Satellite.addRemoteTerminal:  Parameter must be a valid Remote Terminal.")
        if (self.subsystemsList.__len__() == 30):
            raise ValueError("Satellite.addRemoteTerminal:  A Satellite can only house 30 terminals.")
        if (self.subsystemsAddressList.count(rt.getAddress()) == 1):
            raise ValueError("Satellite.addRemoteTerminal:  A Satellite can not house duplicate terminals.")
          
        # Add the instance of the Remote Terminal to our Satellite
        self.subsystemsList.append(rt)
          
        # Add the address of the subsystem to another address list
        self.subsystemsAddressList.append(rt.getAddress())
          
        return self.subsystemsList.__len__()
      
    '''
        Returns a list of all the Remote Terminals
    '''
    def getRemoteTerminals(self):
        return self.subsystemsList
      
    '''
        Returns a list of all the Remote Terminals Addresses
    '''
    def getRemoteTerminalAddresses(self):
        return self.subsystemsAddressList
      
    '''
        Sets the Bus Controller of the Satellite.
    '''
    def setBusController(self, bc=None):
        if (bc == None):
            raise ValueError("Satellite.setBusController:  Parameter must be a valid Bus Controller.")
        if (not isinstance(bc, BusController.BusController)):
            raise ValueError("Satellite.setBusController:  Parameter must be a valid Bus Controller.")
           
        returnedBool = False
           
        if (self.busController == None):
            returnedBool = True
           
        self.busController = bc
        bc.linkWithSatellite(self)
           
        return returnedBool
    
    '''
       Returns the Bus Controller
    '''
    def getBusController(self):
        
        if (self.busController == None):
            raise ValueError("Satellite.getBusController:  No Bus Controller has been set.")
        
        return self.busController
    
    '''
        Signals the bus controller to poll remote terminals.
    '''
    def launch(self, frameCount=1):
        if (frameCount < 0):
            raise ValueError("Satellite.launch:  Parameter greater than or equal to 0.")
        if (not isinstance(frameCount, int)):
            raise ValueError("Satellite.launch:  Parameter must be an integer.")
        
        self.busController.clearWordsWrittenToBus()
        
        for pollIndex in range(0, frameCount):
            self.busController.poll()
            
        return self.busController.getWordsWrittenToBus()
        


















      

         
    