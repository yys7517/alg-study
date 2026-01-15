# 요약:
# 건물주 도현이의 집 N개가 수직선 위에 있음 -> x
# 집 좌표에 공유기를 설치할 것임
# 한 집에 하나의 공유기만을 설치할 수 있음
# "가장 인접한 두 공유기 사이의 거리"를 가능한 크게 하여 설치하려 함

# 찾아야 할 것:
# 각 공유기 간의 거리의 최소를 최대로 하는 공유기 위치
#
# 각 공유기 거리의 최소를 계산하는 방법:
# 1. left와 right를 각각 1, last-first로 지정
# 2. mid를 잡고, 이 mid가 최소의 최대가 될 수 있는 지 확인 시작
    # 2-1. 첫번째 집에 공유기 설치
    # 2-2. 임시 공유기를 그 다음 집에 설치하고 거리 확인
    # 2-3. mid와 마지막 공유기 <-> 임시 공유기 거리 비교
        # 2-3-1. mid보다 거리가 더 먼 경우, 해당 위치에 공유기를 설치하고 count + 1
    # 2-4. 쭉 시도해본 뒤, count의 수가 목표 수보다 큰 지 확인
        # 2-4-1. 목표를 넘긴 경우, 더 큰 mid 값 시도
        # 2-4-2. 목표보다 적은 경우, 더 작은 mid 값 시도
    # 2-5. 최적값 반환

N, C = map(int, input().split())
X = [int(input()) for _ in range(N)]
X.sort()

def binary_search():
    left, right = 1, X[-1]-X[0]
    best = 1
    
    while(left<=right): 
        mid = (left+right) // 2
        last_installed=X[0]
        count = 1
        
        for i in range(1, len(X)):
            try_install = X[i]
            distance = try_install - last_installed
            if distance >= mid:
                last_installed = try_install
                count += 1

        if C <= count:
            left = mid + 1
            best = mid
        else:
            right = mid - 1

    return best

print(binary_search())
                