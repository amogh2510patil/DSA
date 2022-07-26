
class HashTable:
    def __init__(self):
        self.size = 10
        self.arr = [[] for i in range(self.size)]
    
    def get_hash(self,key):
        hash = 0
        for char in key :
            hash += ord(char)
        return hash % self.size
    
    def __setitem__(self,key,value):
        hash = self.get_hash(key)
        for ele in self.arr[hash]:
            if ele[0] == key :
                ele[1] = value
                return
        self.arr[hash].append([key,value])

    
    def __getitem__(self,key):
        hash = self.get_hash(key)
        for ele in self.arr[hash]:
            if ele[0] == key:
                return ele[1]

ht = HashTable()
ht["dd"]=70
ht["dd"] = 420
ht["am"] = 300
ht["aq"] = 500
print(ht.arr)
print(ht['am'])