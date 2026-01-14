# 딕셔너리 사용 풀이
import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

dict = {}

for card in cards:
    if card in dict:
        dict[card] += 1
    else:
        dict[card] = 1

m = int(input())
numbers = list(map(int, input().split()))

for number in numbers:
    if number in dict:
        print(dict[number], end=' ')
    else:
        print(0, end=' ')
