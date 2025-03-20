#Creating a Node class
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#Creating a  Linked list class
class LinkedList:
    def __init__(self):
        self.head=None
    def print(self):
        current_node=self.head #Current_node is considered as head
        while current_node: #While current_node is not null
            print(current_node.data) #Printing the current node data
            current_node=current_node.next #Current node will be equal to the current_node.next to traverse through the linked list
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
    def prepend(self,data):
        new_node=Node(data) #Creating a node object for the data
        new_node.next=self.head #Making the next of the new node as intial head of the linked list
        self.head=new_node #Replacing the head of the linked list with the new node

    def insert(self,prev_node,data):        
        if not prev_node: #Evaluating if the previos node does n't exist or previous node is none
            print("prev_node doesn't exist") #Printing that previos node doesn't exist
            return
        new_node=Node(data) #Creating a node object for the data
        new_node.next=prev_node.next #New_node.next will be assigned to the previous_node.next because the new_node will be inserted
        prev_node.next=new_node #Now the previous node.next will be assigned to the new_node                             
    def delete_node(self, key): #Deleting a node depending on the key value
        cur_node = self.head #Intially, current node is set to equal the head of the linked list
        if cur_node and cur_node.data == key:
            self.head = cur_node.next 
            cur_node = None
            return
        prev_node=None
        while cur_node and cur_node.data != key:
            prev_node=cur_node
            cur_node=cur_node.next
        if cur_node is None:
            print(f"{key} is not present in this linked list")
            return
        prev_node.next=cur_node.next                  
llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.prepend("I")
llist.insert(llist.head.next, "E")
llist.delete_node("B")
llist.delete_node("J")
llist.print()