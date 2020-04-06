# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.
        '''
        # Check if HashTable has enough capacity
        # if self.count >= self.capacity:
        #     self.resize()

        index = self._hash_mod(key)

        # Part 1: Error handling
        # if self.storage[index]:
        #     print(f"Index {index} already exists in the hash table.\nUnable to insert <{key} : {value}>")
        #     return
        
        # Part 2: Linked List Chaining
        if self.storage[index]:
            # Point to tail
            node = self.storage[index]

            while node != None:
                # if the key already exists, overwirte
                if node.key == self._hash(key):
                    node.value = value
                    return
                
                if node.next == None:
                    break
                node = node.next
            
            # Insert the key value pair at the tail
            node.next = LinkedPair(self._hash(key), value)
            self.count += 1
            return
            
        # insert key value pair
        self.storage[index] = LinkedPair(self._hash(key), value)
        self.count += 1



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.
        '''
        # Find the index
        index = self._hash_mod(key)

        # Check if the key exists
        if self.storage[index] == None:
            print(f"Key: {key} does not exists.")
            return
        
        # Remove the value
        head = self.storage[index]
        node = head.next
        prev = head

        # if the first linked list has the key
        if prev.key == key:
            self.storage[index] = node
            self.count -= 1
            return

        while node != None:
            if node.key == self._hash(key):
                prev.next = node.next
                self.count -= 1
                return
            node = node.next
            prev = prev.next

        # All of key value pair in the linked list have been traversed, key was not found
        print(f"Key: {key} does not exists.")


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.
        '''
        # Find index
        index = self._hash_mod(key)

        # Loop through the linked list to find the key
        node = self.storage[index]
        while node != None:
            if node.key == self._hash(key):
                return node.value
            node = node.next
        
        # If the key was not found, return None
        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        '''
        # Double the capacity
        self.capacity *= 2

        # Allocate new memory
        new_storage = [None] * self.capacity

        # Copy the old data into the new storage
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        self.storage = new_storage




# if __name__ == "__main__":
#     ht = HashTable(2)

#     ht.insert("line_1", "Tiny hash table")
#     ht.insert("line_2", "Filled beyond capacity")
#     ht.insert("line_3", "Linked list saves the day!")

#     print("")

#     # Test storing beyond capacity
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     # Test resizing
#     old_capacity = len(ht.storage)
#     ht.resize()
#     new_capacity = len(ht.storage)

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     print("")


ht = HashTable(4)
ht.insert("key1", "1")
ht.insert("key2", "2")
ht.insert("key3", "3")
ht.insert("key4", "4")

print(ht.retrieve("key1"))
print(ht.retrieve("key2"))
print(ht.retrieve("key3"))
print(ht.retrieve("key4"))

ht.insert("key1", "11")
ht.insert("key2", "22")
ht.insert("key3", "33")
ht.insert("key4", "44")

print(ht.retrieve("key1"))
print(ht.retrieve("key2"))
print(ht.retrieve("key3"))
print(ht.retrieve("key4"))