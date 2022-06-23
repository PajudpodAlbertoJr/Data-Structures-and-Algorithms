class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class LList:
    def __init__(self):
        self.head= None

    def push(self,x):
        new_node= Node(x)
        new_node.next = self.head
        self.head = new_node
    def printl(self):
        temp = self.head
        while (temp):
            print(temp.data,end=" ")
            temp = temp.next
#if __name__== '__main__':
llist= LList()
llist.push(3)    
llist.push(3)
llist.printl()
