"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        hash = self.calculate_hash_value(string)

        if not self.table[hash]:
            self.table[hash] = [string]
            return

        for a in self.table[hash]:
            if a == string:
                return
        
        self.table[hash].append(string)

    def lookup(self, string):
        hash = self.calculate_hash_value(string)
        arr = self.table[hash]
        if arr:
            return hash
        return -1

    def calculate_hash_value(self, string):
        
        if len(string) == 0:
            return 0
        
        if len(string) == 1:
            return ord(string)
        
        return ord(string[0]) * 100 + ord(string[1])


# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print(hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
print(hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print(hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print(hash_table.lookup('UDACIOUS'))