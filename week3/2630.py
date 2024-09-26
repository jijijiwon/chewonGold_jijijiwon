N = int(input()) # 전체 종이 한 변의 길이
paper = [list(map(int, input().split())) for _ in range(N)] # N*N 색종이 입력
result = [] # 잘린 색종이의 결과 담을 리스트

white_count = 0
blue_count = 0

def divide(x, y, n):
    global white_count, blue_count
    color = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != color:
                # 색이 다르면 4분할
                half = n // 2
                divide(x, y, half)
                divide(x, y + half, half)
                divide(x + half, y, half)
                divide(x + half, y + half, half)
                return
    # 색이 같으면 카운트 증가
    if color == 0:
        white_count += 1
    else:
        blue_count += 1

divide(0, 0, N)

print(white_count)
print(blue_count)
