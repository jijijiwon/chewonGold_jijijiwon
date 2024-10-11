import sys
from math import gcd
from functools import reduce

# 입력 받기
N = int(sys.stdin.readline())
numbers = []
for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

# 차이들 계산 (각 숫자에서 첫 번째 숫자를 뺀 값들)
differences = [abs(numbers[i] - numbers[0]) for i in range(1, N)]

# 최대 공약수를 리스트 전체에 대해 구하는 함수
def find_gcd_list(nums):
    return reduce(gcd, nums)

# 차이들의 최대 공약수를 구함
gcd_num = find_gcd_list(differences)

# 최대 공약수의 약수들을 찾음
M = []
for i in range(2, gcd_num + 1):
    if gcd_num % i == 0:
        M.append(i)

# 결과 출력
print(*M, sep=" ")
