def hanoi(n, start, end, mid):
    if n == 1:
        print(f"{start} {end}")  # 원판을 start에서 end로 이동
        return
    # N-1개의 원판을 start에서 mid로 이동
    hanoi(n - 1, start, mid, end)
    # 가장 큰 원판을 start에서 end로 이동
    print(f"{start} {end}")
    # N-1개의 원판을 mid에서 end로 이동
    hanoi(n - 1, mid, end, start)

# 입력 받기
N = int(input())

# 이동 과정 출력 여부 결정
total_moves = 2**N - 1
if N <= 20:
    # 총 이동 횟수 출력
    print(total_moves)
    # 하노이탑 이동 과정 출력
    hanoi(N, 1, 3, 2)
else:
    print(total_moves)