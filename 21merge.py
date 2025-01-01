from typing import Optional 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        current_new_LL = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current_new_LL.next = list1
                current_new_LL = list1
                list1 = list1.next
            else:
                current_new_LL.next = list2
                current_new_LL = list2
                list2 = list2.next
        if list1:
            current_new_LL.next = list1
        if list2:
            current_new_LL.next = list2
        return dummy.next

list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

s = Solution()
merged_list = s.mergeTwoLists(list1, list2)

def printList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

printList(merged_list)