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
            print(temp.data,end="  ")
            print()
            temp = temp.next
    def pop(self,x):
        temp = self.head

        if (temp is not None):
            if (temp.data==x):
                self.head = temp.next
                temp = None
                return 
        while(temp is not None):
            if temp.data==x:
                break
            prev = temp
            temp = temp.next

        if (temp == None):
            return
        prev.next = temp.next

        temp = None
#if __name__== '__main__':
llist= LList()
llist.push(3)    
llist.push(3)
llist.push(4)
llist.push(5)
llist.push(6)
llist.push(7)
llist.push(8)

llist.printl()
llist.pop(5)
llist.printl()
