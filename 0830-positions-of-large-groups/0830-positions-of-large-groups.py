class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        answer = [] 
        i = 0 # 그룹의 시작 
        for j in range(len(s)): 
            if j == len(s) -1  or s[j] != s[j+1]:
                if j-i+1 >= 3:
                    answer.append([i,j])
                i = j+1
        return answer