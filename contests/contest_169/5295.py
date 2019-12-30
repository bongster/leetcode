'''
5295. Find N Unique Integers Sum up to Zero

Given an integer n, return any array containing n unique integers such that they add up to 0.

https://leetcode.com/contest/weekly-contest-169/problems/find-n-unique-integers-sum-up-to-zero/
'''
class Solution:
    def sumZero(self, n: int) -> List[int]:
        divide = int(n / 2)
        res = []
        for i in range(1, divide + 1):
            res.extend([i , i * -1])

        if n % 2 != 0:
            res.append(0)
        return res

