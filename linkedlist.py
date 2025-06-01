class Node:
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node
    def get_next(self):
        return self.next_node
    def set_next(self, node):
        self.next_node = node
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data
            
class LinkedList:
    def __init__(self, root = None):
        self.root = root
        self.size = 0
    def get_size(self):
        return self.size
    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1
    def remove(self, data):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == data:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False
    def find(self, data):
        this_node = self.root
        while this_node:
            if this_node.get_data() == data:
                return this_node
            else:
                this_node = this_node.get_next()
        return this_node # Should be None
    def __repr__(self) -> str:
        list = []
        this_node = self.root
        while this_node:
            list.append(this_node.get_data())
            this_node = this_node.get_next()
        return str(list)

ls = LinkedList()

for i in range(10):
    ls.add(2**i)

print(ls)
print(ls.find(4))
print(ls.find(6))
ls.remove(4)
print(ls)
