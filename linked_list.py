class LinkedList(object):
    def __init__(self, head=None):
        self.head = head;

    def add_to_end(self, new_node):
        if(not self.head):
            self.head = new_node
            return
        temp = self.head
        while(temp.next_node):
            temp = temp.next_node
        temp.next_node = new_node
    def print(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next_node


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next_node

    def set_next(new_next):
        self.next_node = new_next


