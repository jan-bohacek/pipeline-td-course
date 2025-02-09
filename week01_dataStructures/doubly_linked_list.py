class Node():
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

def traverseFwd(head):
    while head is not None:
        print(head.value)
        head = head.next

def traverseBwd(tail):
    while tail is not None:
        print(tail.value)
        tail = tail.prev

def insertAfter(prev, value):
    newNode = Node(value)
    if prev.next is not None:
        newNode.next = prev.next
        nextNode = prev.next
        nextNode.prev = newNode
    newNode.prev = prev
    prev.next = newNode
    return newNode







entry_1 = Node(1)
entry_2 = insertAfter(entry_1, 2)
entry_3 = insertAfter(entry_2, 5)
entry_4 = insertAfter(entry_3, 10)

print("Orig list : ")
traverseFwd(entry_1)

entry_a1 = insertAfter(entry_2, 4)
entry_a2 = insertAfter(entry_4, 15)

print("New list : ")
traverseFwd(entry_1)

print("New list backwards : ")
traverseBwd(entry_a2)