#node class
class node:
    def __init__(self, data):
        self.data=data
        self.next=None

#linkedlist class
class LinkedList:
    def __init__(self):  #constructor
        self.head=None
    
    def size(self):  # size of linkedList
        l=0
        temp=self.head
        while temp!=None:
            l=l+1
            temp=temp.next
        print(l)
        return l
    
    def InsertFirst(self,newdata): #insert node at first 
        new_node= node(newdata)
        if self.head is None: #if list is empty 
            self.head=new_node
            return 
        else:
            new_node.next=self.head
            self.head=new_node
    
    def InsertLast(self,newdata): #append node at last 
        new_node=node(newdata)
        if self.head is None:  # if list is empty 
            self.head=new_node
            return 
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=new_node
    
    
    def InsertPos(self,newdata,pos):
        #print(newdata,pos)
        if pos==1:
            self.InsertFirst(newdata)
        else:
            new_node=node(newdata)
            temp=self.head
            prev=None
            for i in range(0,pos-1):
                prev=temp
                temp=temp.next
            if temp!=None:
                new_node.next=temp
                prev.next=new_node
            else: 
                prev.next=new_node

    def printLL(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next

llist=LinkedList()
llist.InsertFirst(1)
llist.InsertLast(4)
llist.InsertPos(2,2)
llist.InsertPos(3,3)
llist.InsertPos(5,3)
llist.printLL()