# **1. 정의**

## 이진 탐색이란?

- **정렬된 탐색 공간**에서 **탐색 범위를 절반씩 줄이며** 정답을 찾는 알고리즘
    
- 시간 복잡도: **O(log N)**

> 핵심은 “배열을 반으로 자른다”가 아니라
> 
> 
> **정답 후보 공간을 반으로 줄인다**는 사고다.
> 

---

# **2. 언제 쓰는가?**

## 이런 질문이 나오면 의심부터 해라

- “최소값의 최대를 구하라”
- “최대값의 최소를 구하라”
- “~할 수 있는가?” (Yes / No 판단)
- 입력 범위가 **10⁹ 이상**인데 완전탐색은 불가능할 때

> 배열이 없어도 이진 탐색을 쓴다.
> 
> 
> **값의 범위**가 탐색 대상일 수 있다. (매개변수 탐색)
> 

---

# **3. 구현 (Python 예시)**

## 기본 이진 탐색 (정렬된 배열)

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

```

## 매개변수 탐색 (결정 문제)

```python
def can_do(mid):
    # mid가 가능하면 True, 아니면 False
    pass

left, right = 1, 10**9
answer = 0

while left <= right:
    mid = (left + right) // 2

    if can_do(mid):
        answer = mid
        left = mid + 1   # 더 큰 값 시도
    else:
        right = mid - 1

print(answer)

```

---

# **4. 코테에서 자주 터지는 포인트 (중요)**

- ❌ **정렬 안 해놓고 이진 탐색**
- ❌ `left < right` / `left <= right` 구분 못 함
- ❌ mid 계산 후 **무한 루프**
- ❌ “최소/최대 중 무엇을 구하는지” 애매한 상태로 구현 시작
- ❌ can_do()가 단조성을 만족하는지 검증 안 함

> 이진 탐색은 조건이 단조(monotonic) 해야만 성립한다.
> 

---

# **5. 실전 꿀팁 (중요)**

- 이진 탐색은 **답을 찾는 알고리즘이 아니라 답을 검증하는 틀**이다.
- 배열 이진 탐색보다 **매개변수 탐색이 실전에서 훨씬 중요**하다.
- 문제를 보면 먼저 이것부터 자문해라:
    - “이게 Yes/No로 판별 가능한가?”
    - “어느 순간부터 불가능해지는가?”

> 이 질문이 성립하면
> 
> 
> 구현 실력 이전에 **이미 절반은 푼 것**이다.
> 
