class Node :
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length =  1

    def printlist(self):
        temp = self.head
        while not temp== None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        if self.head == None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node
            self.length +=  1

    def pop(self):
        temp= self.head
        prev = self.head
        if temp == None:
            print("Nothing to pop")
        if self.head.next == None:
            self.head = None
            self.tail = None
        else:
            while not temp.next == None:
                prev = temp
                temp = temp.next
            
            self.tail = prev 
            self.tail.next = None 
            self.length -=  1
            
            
    def prepend(self, value):
        if self.head == None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def pop_first(self):
        if self.head == None:
            print("Nothing to pop")
        if self.head.next == None:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
            self.length -= 1

    def get(self, index):
        if index < 0 and index > self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp.value

    def set(self, index, value):
        if index < 0 and index > self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            temp.value = value
            

linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(11)
linked_list.append(12)
linked_list.pop()
linked_list.prepend(8)
linked_list.pop_first()
linked_list.printlist()
#print(linked_list.get(2))
print("===================")
linked_list.set(1, 5)
linked_list.printlist()

