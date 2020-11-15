# Given an m x n board of characters and a list of strings words, return all words on the board.
#
# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
#
#  
# Example 1:
#
#
# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
#
#
# Example 2:
#
#
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
#
#
#  
# Constraints:
#
#
# 	m == board.length
# 	n == board[i].length
# 	1 <= m, n <= 12
# 	board[i][j] is a lowercase English letter.
# 	1 <= words.length <= 3 * 104
# 	1 <= words[i].length <= 10
# 	words[i] consists of lowercase English letters.
# 	All the strings of words are unique.
#
#


class Trie:
    def __init__(self):
        self.endOfWord = False
        self.children = [None]*26
    
    def insert(self, word):
        curr = self
        for c in word:
            idx = ord(c) - ord('a')
            if curr.children[idx] == None: curr.children[idx] = Trie()
            curr = curr.children[idx]
        
        curr.endOfWord = True

class Solution:
    def dfs(self, i, j, trie, s):
        c = self.board[i][j]
        if(c == '$'): return
        self.board[i][j] = '$';
        t = trie.children[ord(c) - ord('a')];
        if(t != None):
            ss = s + c;
            if(t.endOfWord): self.result.add(ss);
            if(i < len(self.board)-1): self.dfs(i+1, j, t, ss);
            if(i > 0): self.dfs(i-1, j, t, ss);
            if(j < len(self.board[0])-1): self.dfs(i, j+1, t, ss);
            if(j > 0): self.dfs(i, j-1, t, ss);
        
        self.board[i][j] = c;
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if len(words) == 0: return []
        self.board = board
        trie = Trie()
        for w in words:
            trie.insert(w)
        
        self.result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(i, j, trie, "")
        return list(self.result)
