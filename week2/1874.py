N = int(input())
stack = []
cal = []
k = 1

for _ in range(N):
    num = int(input())
    while k <= num:
        stack.append(k)
        cal.append("+")
        k += 1

    if stack[-1] == num:
        stack.pop()
        cal.append("-")
    else:
        print("NO")
        exit()

print("\n".join(cal))
