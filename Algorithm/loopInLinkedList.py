#!/usr/bin/python
#
#detect and remove loop in a linked list
#
#strategy
#traverse a linked list with two indexes which travel by different steps, let's say m and n(m<n). 
#If there is a loop, the two point will point to the same object.
#
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def addNode(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            pNode = self.head
            qNode = pNode
            while(pNode != None):
                qNode = pNode
                pNode = pNode.next
            qNode.next = newNode
            
    def loopExists(self):
        '''
        return (True, loop_node) if loop exists, otherwise return (False, None)
        '''
        M = 1
        N = 2
        
        if self.head == None:
            return False
        
        mIndex = self.head
        nIndex = self.head
        while mIndex != None and nIndex != None:
            if mIndex != None:
                mIndex = mIndex.next
            else:
                return False
            if nIndex.next != None and nIndex.next.next!= None:
                nIndex = nIndex.next.next
            else:
                return False
            if mIndex == nIndex:
                return (True, mIndex)
                
    def removeLoop(self, node):
        pNode = node

        while pNode.next != node:
            pNode = pNode.next

        pNode.next = None
        

list = LinkedList()
list.addNode(1)
list.addNode(2)
list.addNode(3)
list.addNode(4)
list.addNode(5)
 
#1-2-3-4-5-3
list.head.next.next.next.next.next = list.head.next.next

(exist, node) = list.loopExists()
print("before remove: %s %s" % (exist, node))

if exist:
    list.removeLoop(node)

print("after remove: %s" % list.loopExists())
