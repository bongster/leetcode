# You are given an array arr which consists of only zeros and ones, divide the array into three non-empty parts such that all of these parts represent the same binary value.
#
# If it is possible, return any [i, j] with i + 1 < j, such that:
#
#
# 	arr[0], arr[1], ..., arr[i] is the first part,
# 	arr[i + 1], arr[i + 2], ..., arr[j - 1] is the second part, and
# 	arr[j], arr[j + 1], ..., arr[arr.length - 1] is the third part.
# 	All three parts have equal binary values.
#
#
# If it is not possible, return [-1, -1].
#
# Note that the entire part is used when considering what binary value it represents. For example, [1,1,0] represents 6 in decimal, not 3. Also, leading zeros are allowed, so [0,1,1] and [1,1] represent the same value.
#
#  
# Example 1:
# Input: arr = [1,0,1,0,1]
# Output: [0,3]
# Example 2:
# Input: arr = [1,1,0,1,1]
# Output: [-1,-1]
# Example 3:
# Input: arr = [1,1,0,0,1]
# Output: [0,2]
#
#  
# Constraints:
#
#
# 	3 <= arr.length <= 3 * 104
# 	arr[i] is 0 or 1
#
#


class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        
#         for i in range(n-2):
#             for j in range(i + 1, n):
#                 part1 = "".join([str(i) for i in arr[0:i+1]])
#                 part2 = "".join([str(i) for i in arr[i+1:j]])
#                 part3 = "".join([str(i) for i in arr[j:n]])
#                 print(part1, part2, part3, i, j)
#                 if part1 and part2 and part3 and int(part1, 2) == int(part2, 2) == int(part3, 2):
#                     return [i, j]
#         return [-1, -1]
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A = arr
        c1 = A.count(1)
        if c1%3: return [-1, -1]
        if c1 == 0: return [0, len(A)-1]
        n1 = c1/3
        potential = []
        count = 0
				# find the value of each part
        for a in A[::-1]:
            potential.insert(0, a)
            if a == 1:
                count += 1
                if count == n1:
                    break
        lp = len(potential)
        temp = []
        i = 0
				# find the effective beginning of each part
        while i < (len(A)-lp):
            if A[i] == 1 and A[i:i+lp] == potential:
                temp.append(i)
                i += lp
            elif A[i] == 0:
                i += 1
            else:
                return [-1, -1]
        ans = [temp[0]+lp-1, temp[1]+lp]
        return ans
                
                
