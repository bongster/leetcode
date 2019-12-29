'''
5297. Jump Game III

Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.

https://leetcode.com/contest/weekly-contest-169/problems/jump-game-iii/
'''
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def subCanReach(arr: List[int], start: int, marked: List[bool]):
            if marked[start]:
                return False

            if arr[start] == 0:
                return True

            leftCanReach, rightCanReach = False, False
            marked[start] = True
            if start - arr[start] >= 0:
                leftCanReach = subCanReach(arr, start - arr[start], marked)

            if start + arr[start] < len(arr):
                rightCanReach = subCanReach(arr, start + arr[start], marked)
            return leftCanReach or rightCanReach

        mark = [False] * len(arr)
        res = subCanReach(arr, star, mark)
        return res

