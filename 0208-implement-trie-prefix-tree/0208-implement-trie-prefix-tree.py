class Trie:

    def __init__(self):
        self.trie={}

        

    def insert(self, word: str) -> None:
        current = self.trie 
        for ch in word:
            if ch not in current :
                current[ch]={}
            current = current[ch]
        current['*']=True 
        

    def search(self, word: str) -> bool:
        current = self.trie 
        for  ch in word:
            if ch not in current :

                return False
            current = current[ch]
        return "*" in current


        

    def startsWith(self, prefix: str) -> bool:
        current = self.trie
        for ch in prefix:
            if ch not in current :
                return False
            current = current[ch]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)