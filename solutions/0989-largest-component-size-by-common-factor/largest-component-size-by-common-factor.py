# You are given an integer array of unique positive integers nums. Consider the following graph:
#
#
# 	There are nums.length nodes, labeled nums[0] to nums[nums.length - 1],
# 	There is an undirected edge between nums[i] and nums[j] if nums[i] and nums[j] share a common factor greater than 1.
#
#
# Return the size of the largest connected component in the graph.
#
#  
# Example 1:
#
#
# Input: nums = [4,6,15,35]
# Output: 4
#
#
# Example 2:
#
#
# Input: nums = [20,50,9,63]
# Output: 2
#
#
# Example 3:
#
#
# Input: nums = [2,3,6,7,4,12,21,39]
# Output: 8
#
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 2 * 104
# 	1 <= nums[i] <= 105
# 	All the values of nums are unique.
#
#


class DSU:
    def __init__(self, N):
        self.p = list(range(N))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        self.p[xr] = yr

class Solution:
    def primes_set(self,n):
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return self.primes_set(n//i) | set([i])
        return set([n])

    def largestComponentSize(self, A):
        n = len(A)
        UF = DSU(n)
        primes = defaultdict(list)
        for i, num in enumerate(A):
            pr_set = self.primes_set(num)
            for q in pr_set: primes[q].append(i)

        for _, indexes in primes.items():
            for i in range(len(indexes)-1):
                UF.union(indexes[i], indexes[i+1])

        return max(Counter([UF.find(i) for i in range(n)]).values())
