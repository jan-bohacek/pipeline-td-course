class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def traverseList(head):
    while head is not None:
        print(head.value)
        head = head.next

def insertAt(previous, value):
    newNode = Node(value)
    newNode.next = previous.next
    previous.next = newNode
    return newNode







entry_1 = Node(1)
entry_2 = Node(2)
entry_3 = Node(5)
entry_1.next = entry_2
entry_2.next = entry_3

print("Orig list : ")
traverseList(entry_1)

entry_4 = insertAt(entry_2, 4)
entry_5 = insertAt(entry_3, 15)

print("New list : ")
traverseList(entry_1)