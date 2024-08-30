class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = {}
        
        for r in ransomNote:
            dict[r] = dict.setdefault(r, 0) + 1
        for k, v in dict.items():
            if magazine.count(k) < v:
                return False
        return True


s = Solution()
print(s.canConstruct("a", "b"))
print(s.canConstruct("aa", "aab"))
print(s.canConstruct("a", "bab"))
print(s.canConstruct("aab", "baa"))
print(s.canConstruct("bg", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"))
# 오름차순. 0,1에서 시작 -> 더했을 때 타겟보다 작으면 오른쪽애를 증가. 왼쪽애도 같이 증가
# 타겟보다 크면 왼쪽애를 왼쪽으로.

# 양쪽에서 시작
# 합이 타겟보다 작으면, 왼쪽이 증가, 크면 오른쪽이 차감
