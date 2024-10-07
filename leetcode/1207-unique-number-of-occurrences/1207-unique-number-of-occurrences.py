from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        counter = Counter(arr)
        values = counter.values()
        if len(values) == len(set(values)):
            return True
        return False