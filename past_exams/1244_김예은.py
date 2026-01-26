# 남학생 - 배수이면 토글
# 여학생 - 좌우 대칭이 최대인 구간을 찾아 모두 토글 (스위치의 개수는 홀수)

# 첫째 줄 - 스위치 개수
# 둘째 줄 - 스위치 상태
# 셋쨰 줄 학생 수
# 이후.. (1) - 남학생 수 / (2) - 여학생 수
# ====

# 어떻게 구현할까 (반복문으로 학생 순서대로 남녀 조건마다 스위치 토글)
# 남학생 - 배수마다 토글 -> 쉽다.
# 여학생 - 자기 번호 먼저 토글. 좌우로 확장하면서 좌우 값이 같은지 체크.
    # 범위 안의 값을 모두 토글

# 토글 ^= 이렇게

import sys

def solution(info):
    # 입력값 파싱
    switch_n = int(input()) # 스위치 개수
    switch = list(map(int, input().split())) # 스위치
    m = int(input()) # 학생수

    # 학생 반복
    for _ in range(m):
        gender, num = map(int, input().split())

        # 남학생 
        # (받은 수부터 스위치 전체 개수까지 받은 수만큼)
        if gender == 1:
            for i in range(num-1, switch_n, num):
                switch[i] ^= 1

        # 여학생 
        # (우선 받은 수 토글)
        # (왼쪽 오른쪽 동시에 확장해가며 같은 수인지 확인)
        else:
            switch[num-1] ^= 1
            left = (num - 1) - 1
            right = (num - 1) + 1
    
            # 스위치 범위 내에서 왼&오 같다면
            while left >= 0 and right < switch_n and switch[left] == switch[right]:
                switch[left] ^= 1
                switch[right] ^= 1
                left -= 1
                right += 1
        
        
    return switch

input = sys.stdin.readline
print(solution(input))
