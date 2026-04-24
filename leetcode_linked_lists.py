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

#_________________________________________________________________________________________

#MIDDLE OF LINKED LIST

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
#_________________________________________________________________________________________

#LINKED LIST CYCLE DETECTION

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
            
        return False

#_________________________________________________________________________________________

#DELETE MIDDLE NODE IN A LINKED LIST

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        slow = head
        fast = head
        prev = None
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        prev.next = slow.next
        
        return head

#_________________________________________________________________________________________

# LINK LIST CYCLE II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
        else:
            return None
        
        slow = head
        
        while slow != fast:
            slow = slow.next
            fast = fast.next
            
        return slow
    
#_________________________________________________________________________________________

# REVERSE LINK LIST

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        prev = None
        while temp:
            temp.next,prev,temp=prev,temp,temp.next
        return prev
    
#_________________________________________________________________________________________

#MERGE NODES IN BETWEEN ZEROS

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        tail=dummy
        current=head.next
        total=0
        
        while current:
            if current.val==0:
                tail.next=ListNode(total)
                tail=tail.next
                total=0
            else:
                total+=current.val
            current=current.next
        return dummy.next    
    
#_________________________________________________________________________________________

# ADD TWO NUMBERS

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        tail=dummy
        carry=0
        
        while l1 or l2 or carry:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0
            
            total=val1+val2+carry
            carry=total//10
            digit=total%10
            
            tail.next=ListNode(digit)
            tail=tail.next
            
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
                
        return dummy.next
    
#_________________________________________________________________________________________

#INTERSECTION OF TWO LINKED LISTS

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        ptrA = headA
        ptrB = headB
        
        while ptrA != ptrB:
            ptrA = ptrA.next if ptrA else headB
            ptrB = ptrB.next if ptrB else headA
            
        return ptrA
    
    class Solution:
        def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
            a=headA
            b=headB
            while a!=b:
                a=a.next if a else headB
                b=b.next if b else headA
            return a
    
#_________________________________________________________________________________________
        