class Node:
    def __init__(self, endOfWord = False, char = ""):
        self.endOfWord = endOfWord
        self.char = char
        self.children = {}

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr_node = self.root
        word_idx = 0
        while word_idx < len(word):
            curr_char = word[word_idx]
            if curr_char in curr_node.children:
                curr_node = curr_node.children[curr_char]
            else:
                new_node = Node(False, curr_char)
                curr_node.children[curr_char] = new_node
                curr_node = new_node
            word_idx += 1
        curr_node.endOfWord = True

    def search(self, word: str) -> bool:
        curr_node = self.root
        word_idx = 0
        while word_idx < len(word):
            curr_char = word[word_idx]
            if curr_char in curr_node.children:
                curr_node = curr_node.children[curr_char]
                word_idx += 1
            else:
                return False
        return curr_node.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        prefix_idx = 0
        while prefix_idx < len(prefix):
            curr_char = prefix[prefix_idx]
            if curr_char in curr_node.children:
                curr_node = curr_node.children[curr_char]
                prefix_idx += 1
            else:
                return False
        return True
        