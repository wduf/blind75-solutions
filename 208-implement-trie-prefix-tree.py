# 45.05% time
# 15.63% memory

class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        ln = len(word)
        
        def f(node: TrieNode, i: int) -> None:
            if i == ln:
                node.end = True
                return
            c = word[i]
            i += 1
            if c in node.children:
                f(node.children[c], i)
            else:
                node.children[c] = TrieNode()
                f(node.children[c], i)
        
        f(self.root, 0)

    def search(self, word: str) -> bool:
        ln = len(word)
        
        def f(node: TrieNode, i: int) -> bool:
            if i == ln:
                return node.end
            c = word[i]
            if c not in node.children:
                return False
            return f(node.children[c], i + 1)
        
        return f(self.root, 0)

    def startsWith(self, pre: str) -> bool:
        ln = len(pre)
        
        def f(node: TrieNode, i: int) -> bool:
            if i == ln:
                return True
            c = pre[i]
            if c not in node.children:
                return False
            return f(node.children[c], i + 1)
        
        return f(self.root, 0)
