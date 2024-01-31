from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        counter = Counter(arr)
        N = len(counter.values())
        value_set = set(counter.values())
        if N == len(value_set):
            return True
        return False