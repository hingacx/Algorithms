import SLL


# Hash functions
def hash_function_1(key: str) -> int:
    """Sample Hash Function"""
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash


def hash_function_2(key: str) -> int:
    """Sample Hash Function"""
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash


class HashTable:
    """Create a hash table using a SLL and chaining."""
    def __init__(self, size, function):
        self.size = size
        self.capacity = 0
        self.hash_function = function
        self.buckets = self.make_buckets()

    def __str__(self) -> str:
        """Return content of hash map in human readable form"""
        out = ""
        for bucket in range(self.size):
            out += str(bucket) + " : " + str(self.buckets[bucket]) + "\n"
        return out

    def make_buckets(self) -> list:
        """Helper function that creates the hashmap."""
        hash_list = []
        for bucket in range(self.size):
            hash_list.append(SLL.SLL())
        return hash_list

    def insert(self, key: str, val: int) -> None:
        """Inserts a value to the hash table. Time complexity O(n^2)."""
        hash = self.hash_function(key)
        idx = hash % self.size
        buckets = self.buckets[idx]
        if buckets is None:
            buckets.add_node(key, val)
            self.capacity += 1
        else:
            for node in range(buckets.count()):
                if buckets.get_node(node)[0] == key:
                    buckets.set_value(key, val)
                    return
            # Adds a new Node key/value pair to the hashmap.
            buckets.add_node(key, val)
            self.capacity += 1

    def remove(self, key: str) -> None:
        """Removes a value from the hash table. Time complexity O(n)."""
        hash = self.hash_function(key)
        idx = hash % self.size
        buckets = self.buckets[idx]
        # Return if the index holds no Nodes.
        if buckets is None:
            return
        else:
            buckets.rem_node(key)
            self.capacity -= 1

    def get_bucket_contents(self, idx: int) -> list:
        """Checks the Bucket's contents and returns a list. Time complexity θ(n^2)."""
        if idx < 0 or idx > self.size-1:
            return [None]
        else:
            buckets = self.buckets[idx]
            count = buckets.count()
            contents = []
            for node in range(count):
                contents.append(buckets.get_node(node))
            return contents

    def get_load_factor(self):
        """Returns the load factor of the hashtable. Time complexity O(1)."""
        return self.capacity/self.size

if __name__ == "__main__":
    hash1 = HashTable(5, hash_function_1)
    hash1.insert("dog", 5)
    hash1.insert("cat", 3)
    print(hash1)
    print(hash1.get_load_factor())