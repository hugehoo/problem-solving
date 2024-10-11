from sys import stdin
from bisect import bisect_right

input = stdin.readline

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    NGE = [-1] * len(A)

    


"""
문제를 제대로 이해못햇네.  문제를 잘 읽자.
오른쪽에 있으면서 큰 동시에 `가장 왼쪽에 있는 수`. not 오른쪽 큰 수 중 가장 작은 수.
5
3 5 4 2 7
N 이 크기 때문에 이중 포문은 안됨.
arr[i+1:] 중에 max
그냥 소팅해놓는것은 어떨까.
2 3 5 7 sort

sort 하지 않고.
마지막 인덱스부터 차례로 순회
마지막 원소부터 차례로 팝하여 다른 배열에 저장.
이 다른배열을 어떻게 저장할것인지, 그냥 어펜드?  아니면 소팅해서 이분탐색?
소팅을 왜해"? 그냥 last_element 보다 큰 수중 가장 작은걸 찾으면 됨.

팝 한 후에 다른 배열에 저장하는건 약간 무리수같다.


맨앞에꺼 팝, 어디에 어펜드?
아예 첨 부터 소팅. 2, 3,5, 7
팝 -> 맨앞꺼 인서트.

"""
