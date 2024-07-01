#hashing
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return " -> ".join(values)

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [LinkedList() for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        self.table[index].insert_end(key)

    def display(self):
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")

# Create a hash table with 5 buckets
hash_table = HashTable(5)

# Insert values into the hash table
values_to_insert = [10, 15, 20, 25, 30, 35, 40]
for value in values_to_insert:
    hash_table.insert(value)

# Display the hash table
hash_table.display()
