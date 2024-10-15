from sys import stdin

input = stdin.readline

if __name__ == '__main__':
    str1 = input().strip()
    str2 = input().strip()
    length2 = len(str2)
    length1 = len(str1)
    lcs = [[0] * (length2 + 1) for _ in range(length1 + 1)]
    for i in range(1, length1 + 1):
        for j in range(1, length2 + 1):
            if str1[i - 1] == str2[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])
    for lc in lcs:
        print(lc)
    print(max(map(max, lcs)))
    
"""
결과는 두 문자열의 길이보다 길 수 없다.
가장 긴 최장 부분 수열이 무엇인지 알 필요 없다.
그냥 길이만 알면 됨.

두 문자열은 꼭 같은 길이일 필요 없다.
결과는 가장 짧은 문자열보다 클 수 없다.



"""
