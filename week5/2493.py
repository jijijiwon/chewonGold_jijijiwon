import sys

N = int(sys.stdin.readline())
tops = list(map(int, sys.stdin.readline().split()))

stack = []

for i in range(N):
    while stack and tops[i] >= tops[stack[-1]]:
        stack.pop()
    if not stack:
        print(0, end=" ")
    else:
        print(stack[-1]+1, end=" ")
    stack.append(i)