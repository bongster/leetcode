# Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.
#
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
#
# You must find a solution with a memory complexity better than O(n2).
#
#  
# Example 1:
#
#
# Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# Output: 13
# Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
#
#
# Example 2:
#
#
# Input: matrix = [[-5]], k = 1
# Output: -5
#
#
#  
# Constraints:
#
#
# 	n == matrix.length == matrix[i].length
# 	1 <= n <= 300
# 	-109 <= matrix[i][j] <= 109
# 	All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
# 	1 <= k <= n2
#
#
#  
# Follow up:
#
#
# 	Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
# 	Could you solve the problem in O(n) time complexity? The solution may be too advanced for an interview but you may find reading this paper fun.
#
#


class HeapSort:
    def __init__(self, heap =[]):
        self.heap = heap
        
    def heapify(self, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        
        if l < n and self.heap[largest] < self.heap[l]:
            largest = l
        
        if r < n and self.heap[largest] < self.heap[r]:
            largest = r
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify(n, largest)
    def sort(self):
        n = len(self.heap)
        for i in range(n //2 -1, -1, -1):
            self.heapify(n, i)
        for i in range(n -1, 0, -1):
            self.heap[i], self.heap[0] = self.heap[0], self.heap[i]
            self.heapify(i, 0)
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = [matrix[i][j] for j in range(len(matrix[0])) for i in range(len(matrix))]
        # print(arr)
        h = HeapSort(arr)
        h.sort()
        return h.heap[k -1]
        
        
