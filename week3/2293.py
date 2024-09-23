import sys

# n: 동전의 종류 수, k: 만들고자 하는 금액
n, k = map(int, input().split()) 
coins = []  # 동전의 종류를 저장할 리스트
num = 0  # 사용되지 않은 변수

# 동전의 종류 입력 받기
for i in range(n):
    coins.append(int(sys.stdin.readline()))  # 각 동전의 가치를 입력받음

# dp 배열 초기화: dp[i]는 i원을 만들 수 있는 경우의 수를 저장
dp = [0] * (k + 1)  
dp[0] = 1  # 0원을 만드는 방법은 아무 동전도 사용하지 않는 1가지 방법

# 각 동전의 가치에 대해 dp 테이블 갱신
for coin in coins:
    # 각 동전으로 만들 수 있는 금액들을 업데이트
    for i in range(coin, k + 1):
        dp[i] += dp[i - coin]  # dp[i]는 dp[i-coin]에 현재 동전을 추가하여 만들 수 있는 경우의 수

# k원을 만드는 경우의 수 출력
print(dp[k])
