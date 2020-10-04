# There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.
#
# You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.
#
# Return a list of groups such that each person i is in a group of size groupSizes[i].
#
# Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.
#
#  
# Example 1:
#
#
# Input: groupSizes = [3,3,3,3,3,1,3]
# Output: [[5],[0,1,2],[3,4,6]]
# Explanation: 
# The first group is [5]. The size is 1, and groupSizes[5] = 1.
# The second group is [0,1,2]. The size is 3, and groupSizes[0] = groupSizes[1] = groupSizes[2] = 3.
# The third group is [3,4,6]. The size is 3, and groupSizes[3] = groupSizes[4] = groupSizes[6] = 3.
# Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].
#
#
# Example 2:
#
#
# Input: groupSizes = [2,1,3,3,3,2]
# Output: [[1],[0,5],[2,3,4]]
#
#
#  
# Constraints:
#
#
# 	groupSizes.length == n
# 	1 <= n <= 500
# 	1 <= groupSizes[i] <= n
#
#


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # Grathering number of members to rooms.
        i = 0
        groups = [ [] for _ in groupSizes ] 
        for j in groupSizes:
            groups[j - 1].append(i)
            i += 1
        
        # Checking over flow exception and resizing array.
        j = 1
        res = []
        for group in groups:
            if not len(group):
                pass
            elif len(group) > j:
                k = 0
                divide_num_group = int(len(group) / j)
                # print('divide_num_group', divide_num_group)
                for _ in range(divide_num_group):
                    # print(k, divide_num_group + 1, group[k: k + j + 1])
                    res.append(group[k: k + j])
                    k += j
            elif len(group):
                res.append(group)
            j += 1
        return res
            
