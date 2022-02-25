import heapq
from collections import deque


# 2. 프로그래머스 2주차 1번 문제
def solution(booked, unbooked):
    current_queue = deque()
    book_heap, unbook_heap = [], []

    for b in booked:
        heapq.heappush(book_heap, b)
    for b in unbooked:
        heapq.heappush(unbook_heap, b)

    # 첫 스타트
    book_init = heapq.heappop(book_heap)
    unbook_init = heapq.heappop(unbook_heap)
    result = []
    if book_init[0] <= unbook_init[0]:
        result.append(book_init[1])
        heapq.heappush(unbook_heap, unbook_init)
    else:
        result.append(unbook_init[1])
        heapq.heappush(book_heap, book_init)

    while book_heap:
        book = heapq.heappop(book_heap)
        result.append(book[1])

    while unbook_heap:
        book = heapq.heappop(unbook_heap)
        result.append(book[1])
    return result


booked = [["09:10", "lee"]]
unbooked = [["09:00", "kim"], ["09:05", "bae"]]
solution(booked, unbooked)
solution([["09:55", "hae"], ["10:05", "jee"]], [["10:04", "hee"], ["14:07", "eom"]])