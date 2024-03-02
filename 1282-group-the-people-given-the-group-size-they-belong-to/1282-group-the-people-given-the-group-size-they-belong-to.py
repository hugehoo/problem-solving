from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        num_dict = defaultdict(list)
        result = []
        for i, v in enumerate(groupSizes):
            num_dict[v].append(i)
            if v == len(num_dict[v]):
                result.append(num_dict[v])
                num_dict[v] = []
        return result