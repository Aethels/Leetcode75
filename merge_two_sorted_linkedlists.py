class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(list1, list2):
        
        dummy = ListNode()
        tail = dummy
      
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
        
            tail = tail.next
    
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
    
        return dummy.next
    
    
    list1 = ListNode(1, ListNode(5, ListNode(8)))
    list2 = ListNode(3, ListNode(6, ListNode(7)))

    
    def printList(head):
        while head:
            print(head.val, end=" ")
            head = head.next
        print()

    print("List 1:")
    printList(list1)
    print("List 2:")
    printList(list2)


    merged = mergeTwoLists(list1, list2)
    print("Merged list:")
    printList(merged)