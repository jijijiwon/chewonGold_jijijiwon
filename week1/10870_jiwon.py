# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.
# n과, n번째까지의 피보나치 수열을 담을 리스트 정의
n = int(input())
fibo = [0] * (n + 1)
# 0부터 시작함으로 n+1개의 숫자 존재

for i in range(n + 1):
    if i <= 1:
        fibo[i] = i # 0, 1번째 피보나치 수는 결정
    else:
        fibo[i] = fibo[i - 1] + fibo[i - 2] # 두번째부터 앞의 두 수를 더함

print(fibo[n])


## 공간복잡도 개선 버전
# n = int(input())

# if n <= 1:
#     print(n)
# else:
#     a, b = 0, 1
#     for _ in range(2, n + 1):
#         a, b = b, a + b

#     print(b)
