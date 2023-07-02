class WordDictionary:

    def __init__(self):
        self.str={}
        self.flag=False

    def addWord(self, word: str) -> None:
        curr=self
        for c in word:
            if c not in curr.str:
                curr.str[c]=WordDictionary()
            # curr.str[c].next=Trie()
            curr=curr.str[c]
        curr.flag=True
        

    def search(self, word: str) -> bool:
        curr=self
        for i,c in enumerate(word):
            if c ==".":
                ans=[]
                for paths in curr.str:
                    ans.append(curr.str[paths].search(word[i+1:]))
                if True in ans:
                    return True
                else:
                    return False
            if c not in curr.str:
                return False
            curr=curr.str[c]
        return curr.flag


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)