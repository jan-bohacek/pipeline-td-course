class Node():
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.list_size = 0

    def print_list_fwd(self):
        current = self.head
        if current == None:
            print("List is empty")
            return
        while current is not None:
            print(current.value)
            current = current.next

    def print_list_bwd(self):
        current = self.tail
        if current == None:
            print("List is empty")
            return
        while current is not None:
            print(current.value)
            current = current.prev

    def insert_head(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
        self.list_size += 1
        return new_node
    
    def insert_tail(self, value):
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
        else:
            self.head = new_node
        self.tail = new_node
        self.list_size += 1
        return new_node

    def insert_after_node(self, prev, value):
        new_node = Node(value)
        if prev is None:
            print("Previous node can't be None.")
            return
        if prev.next is not None:
            new_node.next = prev.next
            next_node = prev.next
            next_node.prev = new_node
        else:
            self.tail = new_node
        new_node.prev = prev
        prev.next = new_node
        self.list_size += 1
        return new_node
    
    def insert_after_value(self, search_value, value):
        current = self.head
        while current:
            if current.value == search_value:
                self.insert_after_node(current, value)
                return
            current = current.next
        print("Value not found")

    def delete_node(self, node):
        if node is None:
            return
        
        if self.head == self.tail == node:
            self.head = None
            self.tail = None
        elif node == self.head:
            next_node = node.next
            if next_node:
                next_node.prev = None
                self.head = next_node
            else:
                self.head = None
        elif node == self.tail:
            prev_node = node.prev
            if prev_node:
                prev_node.next = None
                self.tail = prev_node
            else:
                self.tail = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.list_size -= 1

    def delete_value(self, search_value):
        current = self.head
        while current:
            if current.value == search_value:
                self.delete_node(current)
                return
            current = current.next
        print("Value not found")


    def size(self):
        return self.list_size
        





# dList = DoublyLinkedList()

# entry_1 = dList.insert_head(1)
# entry_2 = dList.insert_after_node(entry_1, 2)
# entry_3 = dList.insert_after_node(entry_2, 5)
# entry_4 = dList.insert_after_node(entry_3, 10)

# print("Orig list : ")
# dList.print_list_fwd()

# entry_a1 = dList.insert_after_node(entry_2, 4)
# entry_a2 = dList.insert_after_node(entry_4, 15)

# entry_b1 = dList.insert_head(-1)
# entry_b2 = dList.insert_tail(20)
# # dList.delete_node(entry_b2)

# print("New list : ")
# dList.print_list_fwd()

# print(f"Head is {dList.head.value} and tail is {dList.tail.value}")

# print("New list backwards : ")
# dList.print_list_bwd()




# massList = DoublyLinkedList()

# list = [x+1 for x in range(100)]
# for i in list:
#     if massList.head is not None:
#         massList.insert_after_node(massList.tail, i)
#     else:
#         massList.insert_head(i)

# massList.insert_after_value(95, 200)
# massList.delete_value(94)
# massList.delete_value(100)
# massList.print_list_fwd()


singleList = DoublyLinkedList()
singleList.insert_head(5)
# singleList.print_list_fwd()
singleList.delete_value(5)
singleList.print_list_fwd()