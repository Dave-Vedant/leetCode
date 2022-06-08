"""
Solution Appraoch:

generate bucket function for spporitng the main hashmap...
generate hash map with put, get, remove function



"""
# FIRST APPROACH: The hashing will be Modulo and bucket collison management is array...
class Bucket:
    def __init__(self):
        self.bucket = []  # [k,v]


    def get(self, key):
        for k,v in self.bucket:
            if k == key:
                return v
        return -1
    

    def update(self, key, value):
        fond = False
        for i, kv in enumerate(self.bucket):   # (1,[k,v])
            if key == kv[0]:
                self.bucket[i] = (key,value)
                found = True
                break

        if not found:
            self.bucket.append((key,value))   #(key,value) tuple


    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]



class HashMap(object):
    def __init__(self):
        self.key_space = 2069             # prime number to reduce collision...
        self.hash_table = [Bucket() for i in range(self.key_sapce)]

    def put(self, key, value):
        hash_key = key % self.key_space
        return self.hash_table[hash_key].update(key, value)

    def get(self, key):
        hash_key = key % self.key_space
        return self.hash_table[hash_key].get(key)
    
    def remove(self,key):
        hash_key = key % self.key_space
        self.hash_table[hash_key].remove(key)

    

    # Time complexity = O(N/K) where, N=number of possible keys, K= number of predefined bucket size (2069)

    # space complexity = O(k + M) where, K = bucketsize (2069), M = uniqeue keys that have been inserted. #of unique(keys)






