# Design a special dictionary with some words that searchs the words in it by a prefix and a suffix.
#
# Implement the WordFilter class:
#
#
# 	WordFilter(string[] words) Initializes the object with the words in the dictionary.
# 	f(string prefix, string suffix) Returns the index of the word in the dictionary, which has the prefix prefix and the suffix suffix. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.
#
#
#  
# Example 1:
#
#
# Input
# ["WordFilter", "f"]
# [[["apple"]], ["a", "e"]]
# Output
# [null, 0]
#
# Explanation
# WordFilter wordFilter = new WordFilter(["apple"]);
# wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = 'e".
#
#
#  
# Constraints:
#
#
# 	1 <= words.length <= 15000
# 	1 <= words[i].length <= 10
# 	1 <= prefix.length, suffix.length <= 10
# 	words[i], prefix and suffix consist of lower-case English letters only.
# 	At most 15000 calls will be made to the function f.
#
#


class Trie: 
    def __init__(self): 
        self.root = {}
    
    def insert(self, i, word): 
        node = self.root 
        for c in word: 
            node = node.setdefault(c, {})
            node["#"] = i
        
    def search(self, word): 
        node = self.root
        for c in word: 
            if c in node: node = node[c]
            else: return -1 
        return node["#"]

class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for i, word in enumerate(words): 
            for k in range(len(word)): 
                key = word[k:] + "$" + word
                self.trie.insert(i, key)
            

    def f(self, prefix: str, suffix: str) -> int:
        key = suffix + "$" + prefix
        return self.trie.search(key)
                
                
                


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
