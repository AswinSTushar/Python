#Linked list

#node creation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):        
        self.head = None       

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def traversal(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")

#deletion of last element
    def pop(self):
        if not self.head:
            print("List is empty")
            return
        if not self.head.next:
            self.head=None
            return
        temp=self.head
        while(temp.next.next):
            temp=temp.next
        temp.next=None
        print("Last element deleted")
        print("The updated list is:",end="-->")

# Test
sll = LinkedList()
sll.traversal()       # None (empty list)
sll.append(5)
sll.append(10)
sll.append(11)
sll.traversal()       # 5->10->11->None
sll.pop()
sll.traversal()

        
        