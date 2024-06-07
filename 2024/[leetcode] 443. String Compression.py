class Solution:
    def compress(self, chars: list[str]) -> int:
        if len(chars) == 1:
            return 1
        
        consecutive = 0
        result = []
        for i, c in enumerate(chars):
            if len(chars) == i + 1:
                if c == chars[i - 1]:
                    consecutive += 1
                    result.append(c)
                    self.sample(consecutive, result)
                    break
                else:
                    result.append(chars[i - 1])
                    self.sample(consecutive, result)
                    result.append(c)
                    result.append(1)
                break
            if c != chars[i + 1]:
                result.append(c)
                if consecutive != 0:
                    result.append(consecutive)  # 0 안넣도록
                consecutive = 0
            else:
                consecutive += 1
        
        return len(result)

    def sample(self, consecutive, result):
        if consecutive != 0:
            if len(str(consecutive)) > 1:
                num = len(str(consecutive))
                while num > 0:
                    result.append("-")
                    num -= 1
            else:
                result.append(consecutive)


s = Solution()
print(s.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
print(s.compress(["a"]))
