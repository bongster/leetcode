# There is a stream of n (idKey, value) pairs arriving in an arbitrary order, where idKey is an integer between 1 and n and value is a string. No two pairs have the same id.
#
# Design a stream that returns the values in increasing order of their IDs by returning a chunk (list) of values after each insertion. The concatenation of all the chunks should result in a list of the sorted values.
#
# Implement the OrderedStream class:
#
#
# 	OrderedStream(int n) Constructs the stream to take n values.
# 	String[] insert(int idKey, String value) Inserts the pair (idKey, value) into the stream, then returns the largest possible chunk of currently inserted values that appear next in the order.
#
#
#  
# Example:
#
#
#
#
# Input
# ["OrderedStream", "insert", "insert", "insert", "insert", "insert"]
# [[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]
# Output
# [null, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]]
#
# Explanation
# // Note that the values ordered by ID is ["aaaaa", "bbbbb", "ccccc", "ddddd", "eeeee"].
# OrderedStream os = new OrderedStream(5);
# os.insert(3, "ccccc"); // Inserts (3, "ccccc"), returns [].
# os.insert(1, "aaaaa"); // Inserts (1, "aaaaa"), returns ["aaaaa"].
# os.insert(2, "bbbbb"); // Inserts (2, "bbbbb"), returns ["bbbbb", "ccccc"].
# os.insert(5, "eeeee"); // Inserts (5, "eeeee"), returns [].
# os.insert(4, "ddddd"); // Inserts (4, "ddddd"), returns ["ddddd", "eeeee"].
# // Concatentating all the chunks returned:
# // [] + ["aaaaa"] + ["bbbbb", "ccccc"] + [] + ["ddddd", "eeeee"] = ["aaaaa", "bbbbb", "ccccc", "ddddd", "eeeee"]
# // The resulting order is the same as the order above.
#
#
#  
# Constraints:
#
#
# 	1 <= n <= 1000
# 	1 <= id <= n
# 	value.length == 5
# 	value consists only of lowercase letters.
# 	Each call to insert will have a unique id.
# 	Exactly n calls will be made to insert.
#
#


class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.ord_stream = [ None ] * n
        for i in range(n):
            self.ord_stream[i] = []
        self.ptr = 0

    def insert(self, id: int, value: str) -> List[str]:
        self.ord_stream[id - 1].append(value)
        if id -1 != self.ptr:
            return []
        
        find = False
        for i in range(self.ptr, self.n):
            if not len(self.ord_stream[i]):
                find = True
                self.ptr = i
                break
        if not find:
            self.ptr = self.n - 1
        return [a[0] for a in self.ord_stream[(id -1): self.ptr + 1] if len(a)]


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)
