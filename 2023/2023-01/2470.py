N = int(input())
numbers = sorted(list(map(int, input().split())), key=lambda x: abs(x))
minimum = float("inf")
answer = []
for idx in range(len(numbers) - 1):
    if abs(numbers[idx] + numbers[idx + 1]) < minimum:
        minimum = abs(numbers[idx] + numbers[idx + 1])
        answer = [numbers[idx], numbers[idx + 1]]
print(*sorted(answer))

"""
서로 다른 2개의 용액 -> 음
포인트는 2개인듯. 

 numbers 의 최대 길이는 10만 
 즉 조합은 시간초과 
 두 수를 더했을 때 가장 0에 가깝게. 
 가장 큰수와 가장 작은수의 합
 작은 수와 큰수의 합
 크건 작건 상관없이 두 수의 합이 0에 가까우면 된다. 
 
 서로 부호가 다르다면, 절대값 크기가 비슷한 것.
서로 부호가 같다면 절대값이 0에 가까운 두 수
 numbers 는 모두 양수일 수도, 음수 일수도 있다. 
 브루트포스 안돼
 정렬할 때 절대값이 작은 순서대로 정렬해야한다. 
그렇게 하면 서로 차이가 비슷한 것끼리 모임. 
어떻게 절대값이 작은 순서대로 저장할 수 있는데? lambda baby

이제 앞 뒤로 더해보면서 저장하다. 그리고 민() 친다.


 
4
-100 1 2 95
 
 ans : 3
"""
