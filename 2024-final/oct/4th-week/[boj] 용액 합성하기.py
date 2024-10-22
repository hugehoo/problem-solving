from sys import stdin

input = stdin.readline

if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    s, e = 0, len(arr) - 1
    ans = arr[s] + arr[e]
    while s < e:
        temp = arr[s] + arr[e]
        if abs(ans) > abs(temp):
            ans = temp
        if temp > 0:
            e -= 1
        elif temp < 0:
            s += 1
        else:
            print(0)
            exit(0)
    print(ans)
    
        
        

"""
5
-101 -3 -1 5 93

두 수를 만들 때 0 에 가까운 수 만들기
min 을 찾을게 아니라 abs() 중에 min 을 찾아야함.
"""
