# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        temp = head
        cnt = 0
        while temp: #Counting total nodes
            cnt += 1
            temp = temp.next

        temp = head
        mid = cnt // 2
        print(mid)
        inc = 0
        while temp: # Returning mid node
            if inc == mid:
                return temp
            temp = temp.next
            inc += 1
