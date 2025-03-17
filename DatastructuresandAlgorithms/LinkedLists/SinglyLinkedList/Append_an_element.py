#Creating a Node class
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#Creating a  Linked list class
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data) #Creating a node object for the data
        if(self.head is None): #If the length of the list is 0 or If there is no head for the linked list,
                                #then the new_node will be head of the linked list
            self.head=new_node
            return
        else:
            last_node=self.head # For traversing through the linked list, last_node is considered as head
            while last_node.next: # Until the last_node.next reaches None
                last_node=last_node.next #Last_node will be assigned to the next element in each iteration
            last_node.next=new_node #Once the while lopp is completed, last_node.next is linked to the new_node
                                    #Already new_node.next is None while creating it
    def print(self):
        current_node=self.head #Current_node is considered as head
        while current_node: #While current_node is not null
            print(current_node.data) #Printing the current node data
            current_node=current_node.next #Current node will be equal to the current_node.next to traverse through the linked list
llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.print()              


