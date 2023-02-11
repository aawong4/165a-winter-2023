## O(1) search

class HashTable:
    ## creates hash table
    def __init__(self,size):
        self.size = size
        self.slots = [None] * self.size ##keys
        self.data = [None] * self.size  ##data
    
    ## puts data in key slot
    def put(self,key,data):
        hash_value = self.hash_function(key, len(self.slots))
        ## stores data in slot if there is none there already
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data    
        ## if there is data in the same slot...
        else:
            ## and is the same key, data gets over-written
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            ## and is different key...
            else:
                ## rehash
                next_slot = self.rehash(hash_value, len(self.slots))
                ## if rehash is empty, then store data
                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                ## if rehash is not empty, then double size of slots
                elif self.slots[next_slot] is not None:
                    self.resize(2 * len(self.slots))
                    ## and add key, data pair
                    self.put(key, data)

    def hash_function(self,key,size):
        return key % size

    def rehash(self,oldhash,size):
        return (oldhash+1) % size
    
    ## resizes hashtable into 'new_size: int'
    def resize(self, new_size):
        old_slots = self.slots
        old_data = self.data

        self.slots = [None] * new_size
        self.data = [None] * new_size

        for i in range(len(old_slots)):
            key = old_slots[i]
            if key is not None:
                value = old_data[i]
                self.put(key, value)
    
    def get(self,key):
        startslot = self.hash_function(key,len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        ## traverse hashtable to find (key, data) pair
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position,len(self.slots))
                if position == startslot:
                    stop = True
        return data

    ## allows for HashTable[i] to return data
    def __getitem__(self,key):
        return self.get(key)

    ## allows HashTable[i] = j to create a (key, data) pair where i: key, j:data
    def __setitem__(self,key,data):
        self.put(key,data)

