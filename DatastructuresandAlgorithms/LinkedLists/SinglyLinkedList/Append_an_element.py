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
#DELETING BY VALUE OF THE ELEMENT                                     
    def delete_node(self, key): #Deleting a node depending on the key value
        cur_node = self.head #Intially, current node is set to equal the head of the linked list
        if cur_node and cur_node.data == key: # Here we are checking whether the linked list is not empty
                                                #and also element we are trying to delete is not head
            self.head = cur_node.next #If the key is equal to head, then we are making the next element as head
            cur_node = None #The current element will be None now
            return #Returning out from the condition
        prev_node=None #To take the previous node information, it is assigned as none in the beginning
        while cur_node and cur_node.data != key: #while the current node is not none an dcurrent node data is not equla to key
            prev_node=cur_node #Previous node will be equal to the current node
            cur_node=cur_node.next #current node will be equal to current node.next
        if cur_node is None: # validating if the current node is None
            print(f"{key} is not present in this linked list") #then printing that the key is not present in the linked list
            return #Returning out from the condition
        prev_node.next=cur_node.next #previous node.next will be equal to the current_node.next as the current node will be deleted
        cur_node=None
#DELETING BY POSITION OF THE ELEMENT
    def delete_posnode(self, pos): #Deleting a node depending on the key value
        cur_node = self.head #Intially, current node is set to equal the head of the linked list
        if cur_node and pos == 0: # Here we are checking whether the linked list is not empty
                                                #and also position is nt 0 which means it is head
            self.head = cur_node.next #If the key is equal to head, then we are making the next element as head
            cur_node = None #The current element will be None now
            return #Returning out from the condition
        prev_node=None #To take the previous node information, it is assigned as none in the beginning
        count=0 #count will be equal to 0
        while cur_node and count != pos: #while the current node is not none and count is not equal to the position
            prev_node=cur_node #Previous node will be equal to the current node
            cur_node=cur_node.next #current node will be equal to current node.next
            count+=1 #count will be incremented by 1
        if cur_node is None: # validating if the current node is None
            print(f"{pos} is not present is out of the length of this linked list") #then printing that the key is not present in the linked list
            return #Returning out from the condition
        prev_node.next=cur_node.next #previous node.next will be equal to the current_node.next as the current node will be deleted
        cur_node=None #curent node will be equal to none
#LENGTH OF A LINKED LIST
    def length(self):
        length=0 #Intially lenth is considered as 0
        current_node=self.head #Current node is equal to the head
        if current_node is None: #If the current node i.e., head is empty thn linked list is empty
            print("This linked list is empty") 
            return
        while current_node: #Until the current node is none
            current_node=current_node.next #current node is eqal to the current_node.next
            length+=1 #length will be incremented by 1
        print(f"The length of linked list is {length}")
#LENGTH OF A LINKED LIST USING RECURSIVE IMPLEMENTATION
    def len_recur(self,node): #Finding th elength of linked list using recusion method. For this, head node will be taken as input
        if(node is None): #if the head node is None, then length of the linked list is 0
            return 0
        return 1+ self.len_recur(node.next) #One is added everytime current node (intially head node) is moved to the next node
    def swap_nodes(self,node_1,node_2):
        if(node_1==node_2):
           return
        prev1_node=None
        curr1_node=self.head
        while curr1_node and curr1_node.data!=node_1:
            prev1_node=curr1_node
            curr1_node=curr1_node.next
        prev2_node=None
        curr2_node=self.head
        while curr2_node and curr2_node.data!=node_2:
            prev2_node=curr2_node
            curr2_node=curr2_node.next
        if not curr1_node or not curr2_node:
            return
        if prev1_node:
            prev1_node.next=curr2_node
        else:
            self.head=curr2_node
        if prev2_node:
            prev2_node.next=curr1_node
        else:
            self.head=curr1_node
        curr1_node.next,curr2_node.next= curr2_node.next,curr1_node.next
    def rev(self):
        prev=None
        cur=self.head
        while cur:
            next=cur.next
            cur.next=prev
            prev=cur
            cur=next
        self.head = prev             

                                        
llist = LinkedList()
llist.append("A")
llist.append("C")
llist.append("D")
llist.prepend("I")
llist.print()
llist.insert(llist.head.next, "B")
llist.print()
llist.delete_node("I")
llist.length()
llist.delete_node("J")
llist.delete_posnode(3)
llist.print()
print("The length of the linked list calculated iteratively is:")
print(llist.len_recur(llist.head))
llist.swap_nodes("B", "C")
print("Swapping nodes B and C that are not head nodes")
llist.print()

llist.swap_nodes("A", "B")
print("Swapping nodes A and B where key_1 is head node")
llist.print()
llist.rev()
print("Reversed linked list is as follows:")
llist.print()