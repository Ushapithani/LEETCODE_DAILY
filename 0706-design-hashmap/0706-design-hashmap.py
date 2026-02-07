class MyHashMap:
    def __init__(self):
        self.map = {}
    
    def put(self, key, value):
        self.map[key] = value
    
    def get(self, key):
        if key in self.map:
            return self.map[key]
        return -1
    
    def remove(self, key):
        if key in self.map:
            del self.map[key]