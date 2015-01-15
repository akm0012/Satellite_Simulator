'''
    Created on Mar 30, 2014
    Last updated on Apr 6, 2014


    This is a test file used to test the Class Data

    @author: Andrew K. Marshall
'''
import unittest

import prod.Data as data

class dataTest(unittest.TestCase):

# Data
# methods: instantiate, setContent, getContent

# Constructor
    '''
        Test: Instantiate Data()
    '''
    def test100_010_InstantiateData(self):
        myData = data.Data()
        
        theResult1 = True
        theResult2 = 0
        
        self.assertEquals(theResult1, isinstance(myData, data.Data))
        self.assertEquals(theResult2, myData.payload)
    # END: test100_010_InstantiateData
    
    '''
        Test: Instantiate Data(1)
    '''
    def test100_020_InstantiateData(self):
        myData = data.Data(1)
        
        theResult1 = True
        theResult2 = 1
        
        self.assertEquals(theResult1, isinstance(myData, data.Data))
        self.assertEquals(theResult2, myData.payload)
    # END: test100_020_InstantiateData
    
    '''
        Test: Instantiate Data(30000)
    '''
    def test100_030_InstantiateData(self):
        myData = data.Data(30000)
        
        theResult1 = True
        theResult2 = 30000
        
        self.assertEquals(theResult1, isinstance(myData, data.Data))
        self.assertEquals(theResult2, myData.payload)
    # END: test100_030_InstantiateData
    
    '''
        Test: Instantiate Data(65536)
    '''
    def test100_040_InstantiateData(self):
        myData = data.Data(65535)
        
        theResult1 = True
        theResult2 = 65535
        
        self.assertEquals(theResult1, isinstance(myData, data.Data))
        self.assertEquals(theResult2, myData.payload)
    # END: test100_040_InstantiateData
    
    '''
        Test: Instantiate Data(-1)
    '''
    def test100_910_InstantiateData(self):
        self.assertRaises(ValueError, data.Data, -1)
    # END: test100_910_InstantiateData
    
    '''
        Test: Instantiate Data(65536)
    '''
    def test100_920_InstantiateData(self):
        self.assertRaises(ValueError, data.Data, 65536)
    # END: test100_920_InstantiateData
    
    '''
        Test: Instantiate Data('a')
    '''
    def test100_930_InstantiateData(self):
        self.assertRaises(ValueError, data.Data, 'a')
    # END: test100_930_InstantiateData
    
    '''
        Test: Instantiate Data('$')
    '''
    def test100_940_InstantiateData(self):
        self.assertRaises(ValueError, data.Data, '$')
    # END: test100_940_InstantiateData
    
# setContent

    '''
        Test: Instantiate Data(). Call setContent(0)
    '''
    def test200_010_setContent(self):
        myData = data.Data()
        
        theResult1 = 0
        theResult2 = 0
                
        self.assertEquals(theResult1, myData.setContent(0))
        self.assertEquals(theResult2, myData.payload) 
    # END: test200_010_setContent
    
    '''
        Test: Instantiate Data(). Call setContent(0)
    '''
    def test200_020_setContent(self):
        myData = data.Data()
        
        theResult1 = 1
        theResult2 = 1
                
        self.assertEquals(theResult1, myData.setContent(1))
        self.assertEquals(theResult2, myData.payload) 
    # END: test200_020_setContent
    
    '''
        Test: Instantiate Data(). Call setContent(30000)
    '''
    def test200_030_setContent(self):
        myData = data.Data()
        
        theResult1 = 30000
        theResult2 = 30000
                
        self.assertEquals(theResult1, myData.setContent(30000))
        self.assertEquals(theResult2, myData.payload) 
    # END: test200_030_setContent
    
    '''
        Test: Instantiate Data(). Call setContent(65535)
    '''
    def test200_040_setContent(self):
        myData = data.Data()
        
        theResult1 = 65535
        theResult2 = 65535
                
        self.assertEquals(theResult1, myData.setContent(65535))
        self.assertEquals(theResult2, myData.payload) 
    # END: test200_040_setContent
    
    '''
        Test: Instantiate Data(5). Call setContent(0)
    '''
    def test200_050_setContent(self):
        myData = data.Data(5)
        
        theResult1 = 0
        theResult2 = 0
                
        self.assertEquals(theResult1, myData.setContent(0))
        self.assertEquals(theResult2, myData.payload) 
    # END: test200_050_setContent
    
    '''
        Test: Instantiate Data(5). Call setContent(65535)
    '''
    def test200_060_setContent(self):
        myData = data.Data(5)
        
        theResult1 = 65535
        theResult2 = 65535
                
        self.assertEquals(theResult1, myData.setContent(65535))
        self.assertEquals(theResult2, myData.payload) 
    # END: test200_060_setContent
    
    '''
        Test: Instantiate Data(). Call setContent(-1)
    '''
    def test200_910_InstantiateData(self):
        myData = data.Data()
        
        self.assertRaises(ValueError, myData.setContent, -1)
    # END: test200_910_InstantiateData
    
    '''
        Test: Instantiate Data(). Call setContent(65536)
    '''
    def test200_920_InstantiateData(self):
        myData = data.Data()
        
        self.assertRaises(ValueError, myData.setContent, 65536)
    # END: test200_920_InstantiateData
    
    '''
        Test: Instantiate Data(). Call setContent('a')
    '''
    def test200_930_InstantiateData(self):
        myData = data.Data()
        
        self.assertRaises(ValueError, myData.setContent, 'a')
    # END: test200_930_InstantiateData
    
    '''
        Test: Instantiate Data(). Call setContent('%')
    '''
    def test200_940_InstantiateData(self):
        myData = data.Data()
        
        self.assertRaises(ValueError, myData.setContent, '%')
    # END: test200_940_InstantiateData
    
    '''
        Test: Instantiate Data(5). Call setContent(-1)
    '''
    def test200_950_InstantiateData(self):
        myData = data.Data(5)
        
        self.assertRaises(ValueError, myData.setContent, -1)
    # END: test200_950_InstantiateData
    
    '''
        Test: Instantiate Data(5). Call setContent(65536)
    '''
    def test200_960_InstantiateData(self):
        myData = data.Data(5)
        
        self.assertRaises(ValueError, myData.setContent, 65536)
    # END: test200_960_InstantiateData
    
    '''
        Test: Instantiate Data(5). Call setContent('a')
    '''
    def test200_970_InstantiateData(self):
        myData = data.Data(5)
        
        self.assertRaises(ValueError, myData.setContent, 'a')
    # END: test200_970_InstantiateData
    
    '''
        Test: Instantiate Data(5). Call setContent('%')
    '''
    def test200_980_InstantiateData(self):
        myData = data.Data(5)
        
        self.assertRaises(ValueError, myData.setContent, '%')
    # END: test200_980_InstantiateData
    
# getContent

    '''
        Test: Instantiate Data(). Call setContent(65535). Call getContent()
    '''
    def test300_010_getContent(self):
        myData = data.Data()
        
        theResult1 = 65535
        theResult2 = 65535
                
        self.assertEquals(theResult1, myData.setContent(65535))
        self.assertEquals(theResult2, myData.getContent()) 
    # END: test300_010_getContent
    
    '''
        Test: Instantiate Data(5). Call setContent(65535) Call getContent()
    '''
    def test300_020_setContent(self):
        myData = data.Data(5)
        
        theResult1 = 65535
        theResult2 = 65535
                
        self.assertEquals(theResult1, myData.setContent(65535))
        self.assertEquals(theResult2, myData.getContent()) 
    # END: test300_020_setContent
    
    '''
        Test: Instantiate Data(). Call getContent()
    '''
    def test300_030_getContent(self):
        myData = data.Data()
        
        theResult2 = 0
                
        self.assertEquals(theResult2, myData.getContent()) 
    # END: test300_030_getContent
    
    '''
        Test: Instantiate Data(5). Call setContent(1) Call getContent()
    '''
    def test300_040_getContent(self):
        myData = data.Data(1)
        
        theResult1 = 1
        theResult2 = 1
                
        self.assertEquals(theResult1, myData.setContent(1))
        self.assertEquals(theResult2, myData.getContent()) 
    # END: test300_040_getContent
    
    '''
        Test: Instantiate Data(). Call setContent(30000). Call getContent()
    '''
    def test300_050_setContent(self):
        myData = data.Data()
        
        theResult1 = 30000
        theResult2 = 30000
                
        self.assertEquals(theResult1, myData.setContent(30000))
        self.assertEquals(theResult2, myData.getContent()) 
    # END: test300_050_setContent
    
    '''
        Test: Instantiate Data(5). Call setContent(0) Call getContent()
    '''
    def test300_060_getContent(self):
        myData = data.Data(5)
        
        theResult1 = 0
        theResult2 = 0
                
        self.assertEquals(theResult1, myData.setContent(0))
        self.assertEquals(theResult2, myData.getContent()) 
    # END: test300_060_getContent
    
    
    
    
