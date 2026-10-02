class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.val

    def insertHead(self, val: int) -> None:
        node = Node(val, self.head)
        self.head = node
        if self.tail is None:
            self.tail = node
        self.size += 1

    def insertTail(self, val: int) -> None:
        node = Node(val)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False

        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next
            prev.next = prev.next.next
            if prev.next is None:
                self.tail = prev

        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        result = []
        cur = self.head
        while cur:
            result.append(cur.val)
            cur = cur.next
        return result
