# A linked list is a sequence of data element, which are connected together link
# each data connection of another data element
# Creation linked list
class Node:
    def __init__(self,dataval = None):
        self.dataval = dataval
        self.nextval = None
class SLinkedList:
    def __init__(self):
        self.headval = None
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
    def AtBeggining(self,newdata):
        NewNode = Node(newdata)
#         updating the new nodes next val to existing node
        NewNode.nextval = self.headval
        self.headval = NewNode
    def AtEnd(self,newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nexval = NewNode
# object creating
list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# link first node to second node
list.headval.nextval = e2

# link 2nd node to 3rd node
e2.nextval = e3

# travaersing
# list.listprint()
list.listprint()

# instertion
list.AtBeggining("sun")
list.listprint()

# insertion at the end
list.AtEnd("Thur")
list.listprint()