
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_to_beginning(self,data):
        temp = self.head
        self.head = Node(data,temp)

    def add_to_end(self,data):
        if self.head is None:
            self.head = Node(data)
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data)

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        temp = self.head
        while temp:
            dat = temp.data
            print(dat,end="-->")
            temp = temp.next
        print()

    def insert_vals(self,lst):
        self.head = None
        for l in lst:
            self.add_to_end(l)
    
    def get_len(self):
        if self.head is None:
            return 0
        
        count  = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count
    
    def remove_at(self,index):
        if index < 0 or index >= self.get_len():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next
            return
        temp = self.head
        for i in range(0,index-1):
            temp = temp.next
        temp.next = temp.next.next
        return

    def insert_at(self,index,data):
        if index < 0 or index > self.get_len():
            raise Exception("invalid index")
        
        if index == 0:
            self.add_to_beginning(data)
            return
        
        temp = self.head
        for i in range(0,index-1):
            temp = temp.next
        
        node = Node(data,temp.next)
        temp.next = node
        return



ll = LinkedList()
ll.add_to_beginning(1)
ll.print()
ll.add_to_beginning(10)
ll.print()
ll.add_to_beginning(20)
ll.print()
ll.add_to_end(420)
ll.print()

ll.insert_vals(["Netherlands","Germany","Spain","France"])
ll.print()

print(ll.get_len())
ll.remove_at(3)
ll.print()

ll.insert_at(0,"England")
ll.print()

ll.insert_at(3,"Port")
ll.print()