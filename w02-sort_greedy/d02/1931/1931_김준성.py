"""
빠른 입력, time complexity 줄임

goal -> 회의수 최대값
outline:
    - 회의는 안겹치게
    - 중단 불가
    - 회의 시작 과 끝나는 시간이 같을수 있다. (시작하자마자 끝남)

"""

import sys

# 회의 수 입력값
N = int(sys.stdin.readline())

# N + 1 줄까지 시작과 끝나는 시간 i.e. 1 10

meeting = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
meeting_length = []
counter = 0


# 일찍 시작하는 미팅부터 배열
meeting.sort(reverse=False)
print(meeting)

# 미팅 시간 따로 구해서 array 에 append
for i in range(len(meeting)):
    diff = meeting[i][1] - meeting[i][0]
    print("meeting", diff)

    if ((meeting[i][1] >= meeting[i - 1][1]) and N > 0):
        N = N - diff
        counter += 1
        print(N)


       




