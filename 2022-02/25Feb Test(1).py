import heapq
from collections import deque


# 2. 프로그래머스 2주차 1번 문제
def heappopAll(heap : heapq, result):
    while heap:
        temp = heapq.heappop(heap)
        result.append(temp[1])
    pass


def solution(booked, unbooked):
    current_queue = deque()
    book_heap, unbook_heap = [], []

    for b in booked:
        heapq.heappush(book_heap, b)
    for b in unbooked:
        heapq.heappush(unbook_heap, b)

    # time 을 10분단위로 추가해줄 함수 필요.
    # cuurent_queue 가 비어있다면, 그 다음으로 들어올 시간에 맞춰 time 을 다시 초기화해줄 필요 있다.

    # 첫 스타트
    book_init = heapq.heappop(book_heap)
    unbook_init = heapq.heappop(unbook_heap)
    result = []
    if book_init[0] <= unbook_init[0]:
        result.append(book_init[1])
        current_time = time_calculate(book_init[0])
        heapq.heappush(unbook_heap, unbook_init)
    else:
        result.append(unbook_init[1])
        current_time = time_calculate(unbook_init[0])
        heapq.heappush(book_heap, book_init)

    # 1번 비교 :  book_heap 의 첫번째가 current_time 보다 작거나 같다면 book_heap 을 pop하고 result 에 넣는다.
    # 2번 비교 : current_time 보다 book_heap 첫번째가 높은데, unbook_heap 의 첫번째가 book_heap 보다 더 빠르다면 unbook_heap 을 pop 하고 result 에 넣는다.
    while book_heap or unbook_heap:
        # book heap 이 없다면, 걍 unbook heap 만 출력시키면 됨
        if book_heap:
            book = heapq.heappop(book_heap)
        else:
            heappopAll(unbook_heap, result)
            break

        if unbook_heap:
            unbook = heapq.heappop(unbook_heap)
        else:
            heappopAll(book_heap, result)
            break

        if current_time >= book[0]:
            result.append(book[1])
            current_time = time_calculate(book[0])
            heapq.heappush(unbook_heap, unbook)
        elif current_time < book[0] and unbook[0] < book[0]:
            result.append(unbook[1])
            current_time = time_calculate(unbook[0])
            heapq.heappush(book_heap, book)
        else:
            result.append(book[1])
            current_time = time_calculate(book[0])
            heapq.heappush(unbook_heap, unbook)

    return result


def make_two_string(num: int):
    return str(num) if len(str(num)) == 2 else '0' + str(num)


def calculate_minute(minute: str):
    return make_two_string(int(minute[-1]))


def calculate_hour(hour: str):
    if int(hour) + 1 > 23:
        return "00"
    else:
        return make_two_string(int(hour) + 1)


def time_calculate(time: str):
    hour, minute = time.split(":")
    if int(minute) + 10 >= 60:
        hour = calculate_hour(hour)
        minute = calculate_minute(minute)
    else:
        minute = make_two_string(int(minute) + 10)

    return ':'.join([hour, minute])


solution([["09:10", "lee"]], [["09:00", "kim"], ["09:05", "bae"]])
# solution([["09:55", "hae"], ["10:05", "jee"]], [["10:04", "hee"], ["14:07", "eom"]])
# solution([["09:55", "hae"], ["10:05", "jee"], ["15:05", "kwo"]], [["10:04", "hee"], ["14:07", "eom"], ["23:50", "eom"]])
