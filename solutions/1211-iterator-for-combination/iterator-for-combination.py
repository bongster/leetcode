# Design the CombinationIterator class:
#
#
# 	CombinationIterator(string characters, int combinationLength) Initializes the object with a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
# 	next() Returns the next combination of length combinationLength in lexicographical order.
# 	hasNext() Returns true if and only if there exists a next combination.
#
#
#  
# Example 1:
#
#
# Input
# ["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
# [["abc", 2], [], [], [], [], [], []]
# Output
# [null, "ab", true, "ac", true, "bc", false]
#
# Explanation
# CombinationIterator itr = new CombinationIterator("abc", 2);
# itr.next();    // return "ab"
# itr.hasNext(); // return True
# itr.next();    // return "ac"
# itr.hasNext(); // return True
# itr.next();    // return "bc"
# itr.hasNext(); // return False
#
#
#  
# Constraints:
#
#
# 	1 <= combinationLength <= characters.length <= 15
# 	All the characters of characters are unique.
# 	At most 104 calls will be made to next and hasNext.
# 	It is guaranteed that all calls of the function next are valid.
#
#


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combs = deque()
        def combinations(cur, idx):
            if len(cur) == combinationLength:
                self.combs.append(''.join(cur))
                return
            for i in range(idx, len(characters)):
                cur.append(characters[i])
                combinations(cur, i + 1)
                cur.pop()
        combinations([], 0)
    def next(self) -> str:
        return self.combs.popleft()

    def hasNext(self) -> bool:
        return len(self.combs) > 0
            
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()