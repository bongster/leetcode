# Design a data structure that supports adding new words and finding if a string matches any previously added string.
#
# Implement the WordDictionary class:
#
#
# 	WordDictionary() Initializes the object.
# 	void addWord(word) Adds word to the data structure, it can be matched later.
# 	bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
#
#
#  
# Example:
#
#
# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]
#
# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
#
#
#  
# Constraints:
#
#
# 	1 <= word.length <= 25
# 	word in addWord consists of lowercase English letters.
# 	word in search consist of '.' or lowercase English letters.
# 	There will be at most 3 dots in word for search queries.
# 	At most 104 calls will be made to addWord and search.
#
#


class TrieNode:
    def __init__(self, end=False):
        self.end = end
        self.children = {}
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def add(self, word):
        curr = self.root
        for c in word:
            if not c in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True
    def search(self, word):
        wi = len(word)
        def dfs(node, i):
            if i == wi:
                return node.end
            if word[i] == '.':
                for child in node.children:
                    if dfs(node.children[child], i + 1):
                        return True
            if word[i] in node.children:
                if dfs(node.children[word[i]], i + 1):
                    return True
            return False
        return dfs(self.root, 0)


class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.add(word)

    def search(self, word: str) -> bool:
        return self.trie.search(word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
