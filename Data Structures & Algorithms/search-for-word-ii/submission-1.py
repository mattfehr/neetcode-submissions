class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True
    
    def search(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.endOfWord

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.add(word)
        seen = set()
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        root = trie.root
        sol = []
        
        def dfs(row, col, curr, word):
            char = board[row][col]
            if char not in curr.children or (row,col) in seen:
                return
            
            curr = curr.children[char]
            seen.add((row,col))
            word.append(char)
            if curr.endOfWord:
                sol.append("".join(word))
                curr.endOfWord = False #avoid dupes

            for dr, dc in dirs:
                nr, nc = row+dr, col+dc
                if nr < 0 or nc < 0 or nr >= len(board) or nc >= len(board[0]):
                    continue
                dfs(row+dr, col+dc, curr, word[:])
            
            seen.remove((row,col))
            word.pop()

        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, root, [])
        return sol









