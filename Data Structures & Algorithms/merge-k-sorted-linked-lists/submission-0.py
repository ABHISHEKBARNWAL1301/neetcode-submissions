# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for ls in lists:
            while ls:
                nodes.append(ls.val)
                ls = ls.next
        
        nodes.sort()
        curr = res =  ListNode(0)
        for node in nodes:
            curr.next = ListNode(node)
            curr = curr.next

        return res.next