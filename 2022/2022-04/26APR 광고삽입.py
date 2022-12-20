def solution(play_time, adv_time, logs):
    logs_start_sec = [0] * len(logs)
    logs_end_sec = [0] * len(logs)

    play_time_sec = str_to_int(play_time)
    total_time = [0 for i in range(play_time_sec + 1)]

    most_view = 0
    max_time = 0
    # total_time 이라는 전체 시간에 각 사용자의 시작, 끝 시간별 시청 횟수를 기록했다.
    # 만약 1초에 시작한 사람이 둘이라면 해당 인덱스의 값은 2가 된다.
    for idx, log in enumerate(logs):
        start, end = log.split("-")
        logs_start_sec[idx] = str_to_int(start)
        logs_end_sec[idx] = str_to_int(end)
        total_time[logs_start_sec[idx]] += 1
        total_time[logs_end_sec[idx]] -= 1

    adv_time_sec = str_to_int(adv_time)
    for i in range(1, len(total_time)):  # 3
        total_time[i] = total_time[i] + total_time[i - 1]

    for i in range(1, len(total_time)):  # 4
        total_time[i] = total_time[i] + total_time[i - 1]

    for i in range(adv_time_sec - 1, play_time_sec):
        if i >= adv_time_sec:
            if most_view < total_time[i] - total_time[i - adv_time_sec]:
                most_view = total_time[i] - total_time[i - adv_time_sec]
                max_time = i - adv_time_sec + 1
        else:
            if most_view < total_time[i]:
                most_view = total_time[i]
                max_time = i - adv_time_sec + 1
    return int_to_str(max_time)


def int_to_str(time):
    h = time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    time = time % 3600
    m = time // 60
    m = '0' + str(m) if m < 10 else str(m)
    time = time % 60
    s = '0' + str(time) if time < 10 else str(time)
    return h + ':' + m + ':' + s


def str_to_int(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


print(solution("02:03:55", "00:14:15",
               ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29",
                "01:37:44-02:02:30"]))
