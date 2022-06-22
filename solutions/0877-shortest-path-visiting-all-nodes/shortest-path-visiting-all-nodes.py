# You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.
#
# Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.
#
#  
# Example 1:
#
#
# Input: graph = [[1,2,3],[0],[0],[0]]
# Output: 4
# Explanation: One possible path is [1,0,2,0,3]
#
#
# Example 2:
#
#
# Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
# Output: 4
# Explanation: One possible path is [0,1,4,2,3]
#
#
#  
# Constraints:
#
#
# 	n == graph.length
# 	1 <= n <= 12
# 	0 <= graph[i].length < n
# 	graph[i] does not contain i.
# 	If graph[a] contains b, then graph[b] contains a.
# 	The input graph is always connected.
#
#


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
#         def dfs(i, used, path, res):
#             if len(set(path)) == len(graph):
#                 res.append(path)
#                 return
#             for x in graph[i]:
#                 if [i, x] not in used:
#                     used.append([i, x])
#                     y = dfs(x, used, path + [i], res)
#                     used.pop()
        
        memo, final, q, steps = set(), (1 << len(graph)) - 1, [(i, 1 << i) for i in range(len(graph))], 0
        while True:
            new = []
            for node, state in q:
                if state == final: return steps
                for v in graph[node]:
                    if (state | 1 << v, v) not in memo:
                        new.append((v, state | 1 << v))
                        memo.add((state | 1 << v, v))
            q = new
            steps += 1
        
#         res = []
#         for i in range(len(graph)):
#             dfs(i, [], [], res)
        
#         if len(res):
#             return min([len(x) for x in res]) - 1
#         else:
#             return 0
        
