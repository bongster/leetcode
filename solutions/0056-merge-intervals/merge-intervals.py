# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
#
#  
# Example 1:
#
#
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
#
#
# Example 2:
#
#
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#
#
#  
# Constraints:
#
#
# 	1 <= intervals.length <= 104
# 	intervals[i].length == 2
# 	0 <= starti <= endi <= 104
#
#


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        print(intervals)
        intervals.sort(key=lambda x: x[0])
        print(intervals)
        n = len(intervals)
        k = 0
        while len(intervals):
            i, intervals = intervals[0], intervals[1:]
            ep = i[1]
            while len(intervals):
                j = intervals[0]
                if j[0] <= ep:
                    ep = max(ep, j[1])
                    intervals = intervals[1:]
                else:
                    break

            res.append([i[0], ep])
        return res
