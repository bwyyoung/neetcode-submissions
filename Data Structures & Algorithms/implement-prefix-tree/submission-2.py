class PrefixTree:
    class TrieNode:
        def __init__(self):
            self.branch = [None] * 26
            self.endword = False

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word: str) -> None:        
        current = self.root
        for c in word:
            index = ord(c) - ord('a')
            if current.branch[index] is None:
                current.branch[index] = self.TrieNode()
            current = current.branch[index]
        current.endword = True


    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            index = ord(c) - ord('a')
            if current is None:
                return False
            if current.branch[index] is None:
                return False
            current = current.branch[index]

        return current.endword

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if current is None:
                return False
            if current.branch[index] is None:
                return False
            current = current.branch[index]
        return True
        