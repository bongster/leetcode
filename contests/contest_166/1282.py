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

