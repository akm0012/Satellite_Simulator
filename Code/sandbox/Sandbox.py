'''
Created on Apr 20, 2014

@author: Andrew
'''

import CA04.prod.RemoteTerminal as RT
import CA05.prod.Satellite as SAT

myRemTerm = RT.RemoteTerminal(5)
myRemTerm2 = RT.RemoteTerminal(5)

mySat = SAT.Satellite()

mySat.addRemoteTerminal(myRemTerm)
# mySat.addRemoteTerminal(myRemTerm)



myList = [myRemTerm]

print myList.count(myRemTerm.getAddress())

# myListAddress = [myRemTerm.getAddress(), myRemTerm2.getAddress()]

# print myListAddress.count(myRemTerm.getAddress())

list2 = [1, 2, 3]

print len(list2)