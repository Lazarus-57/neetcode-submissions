class Trienode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = Trienode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trienode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:

        def dfs(index, cur):
            
            if index == len(word):
                return cur.endOfWord
            
            c = word[index]
            
            if c == '.':
                for child in cur.children.values():
                    if dfs(index + 1, child):
                        return True
                return False 
            else:
                if c not in cur.children:
                    return False
                return dfs(index + 1, cur.children[c])

        return dfs(0, self.root)