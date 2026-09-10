
class ListNode():
    def __init__(self, key: int):
        self.val = key
        self.next = None 

class MyHashSet:

    def __init__(self):
        self.data = [ListNode(0)]*1000001


    def add(self, key: int) -> None:
        curr = self.data[key%100]
        while curr.next:
            if curr.next.val == key:
                return
            curr = curr.next
        curr.next = ListNode(key)


    def remove(self, key: int) -> None:
        curr = self.data[key%100]
        while curr and curr.next:
            if curr.next.val == key:
                curr.next  = curr.next.next
                return
            curr = curr.next
            

    def contains(self, key: int) -> bool:
        curr = self.data[key%100]
        while curr.next:
            if curr.next.val == key:
                return True
            curr = curr.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)