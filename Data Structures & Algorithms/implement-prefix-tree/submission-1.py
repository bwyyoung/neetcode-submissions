class PrefixTree:
    class TrieNode:
        def __init__(self):
            self.branch = [None] * 26
            self.endword = False

    def __init__(self):
        self.root = None

    def insert(self, word: str) -> None:
        if self.root is None:
                self.root = self.TrieNode()
        current = self.root
        for c in word:
            index = ord(c) - ord('a')
            print(f"insert {c}   {index} ")
            if current.branch[index] is None:
                current.branch[index] = self.TrieNode()
            current = current.branch[index]
        current.endword = True


    def search(self, word: str) -> bool:
        current = self.root
        print(f"searching {word}")
        for c in word:
            index = ord(c) - ord('a')
            print(f"search {c}   {index} ")
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
        