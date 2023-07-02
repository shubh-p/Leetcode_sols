class Trie:

    def __init__(self):
        self.str={}
        self.flag=False
        # self.next=None

    def insert(self, word: str) -> None:
        curr=self
        for c in word:
            if c not in curr.str:
                curr.str[c]=Trie()
            # curr.str[c].next=Trie()
            curr=curr.str[c]
        curr.flag=True

    def search(self, word: str) -> bool:
        curr=self
        for c in word:
            if c not in curr.str:
                return False
            curr=curr.str[c]
        return curr.flag
            

    def startsWith(self, prefix: str) -> bool:
        curr=self
        for c in prefix:
            if c not in curr.str:
                return False
            curr=curr.str[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)