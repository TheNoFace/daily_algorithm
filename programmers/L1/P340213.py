# https://school.programmers.co.kr/learn/courses/30/lessons/340213
# [PCCP 기출문제] 1번 / 동영상 재생기


def solution(video_len, pos, op_start, op_end, commands):
    pos = to_seconds(pos)

    for command in commands:
        if is_opening(pos, op_start, op_end):
            pos = to_seconds(op_end)

        if command == "next":
            # 남은 시간이 10초 이상일 경우
            if to_seconds(video_len) - pos >= 10:
                pos = (
                    pos + 10
                    if not is_opening(pos + 10, op_start, op_end)
                    else to_seconds(op_end)
                )
            # 남은 시간이 10초 미만일 경우
            else:
                pos = to_seconds(video_len)
        elif command == "prev":
            # 현재 위치가 10초 이상일 경우
            if pos >= 10:
                pos = (
                    pos - 10
                    if not is_opening(pos - 10, op_start, op_end)
                    else to_seconds(op_end)
                )
            # 현재 위치가 10초 미만일 경우
            else:
                pos = 0

    return to_hhmm(pos)


def is_opening(seconds, op_start, op_end):
    return to_seconds(op_start) <= seconds <= to_seconds(op_end)


def to_seconds(time):
    time = list(map(int, time.split(":")))
    return time[0] * 60 + time[1]


def to_hhmm(time):
    minutes = "0" + str(time // 60) if time // 60 < 10 else str(time // 60)
    seconds = "0" + str(time % 60) if time % 60 < 10 else str(time % 60)
    return minutes + ":" + seconds
