from collections import Counter


class Solution(object):
    def countNumber(self, num):
        q, r, = divmod(num, 3)
        if q < 1:
            return 1
        
        if q >= 1 and r == 0:
            return q
        
        if q >= 1 and r > 0:
            return 1 + q
    
    def minimumRounds(self, tasks):
        result = 0
        counter = Counter(tasks)
        for c in counter:
            if counter[c] < 2:
                return -1
            result += self.countNumber(counter[c])
        return result

        
"""
같은 수 끼리 묶어버릴까
2, 3씩 제거하기. 
1개만 남으면 안된다.
어떤방법이 최소 인지 파악하는게 관건. 
최초에 몇개가 남아있느냐에 따라 다를듯. 
1개 -> x
2 -> 1
3 -> 1
4 -> 2
5 -> 2
6 -> 2
7 -> 3
8 -> 3
9 -> 3
10 -> 4
11 -> 4
12 -> 4
13 -> 5
14 -> 5
15 -> 5
16 -> 6
17 -> 6
18 -> 6
19 -> 7
dict -> key : count 만들기. 
count 별로 함수에 넣기. 
함수는 count 를 인풋으로 받아 몇번만에 없앨 수 있는지 dp 로 리턴. 

"""