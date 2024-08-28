# strings = list(input())
# N = int(input())
# cursor = len(strings)

# for i in range(N):
#     command = input().split()

#     if command[0] == "L" and cursor > 0:
#         cursor -= 1
#     elif command[0] == "D" and cursor < len(strings):
#         cursor += 1
#     elif command[0] == "B" and cursor > 0:
#         del strings[cursor - 1]
#         cursor -= 1
#     elif command[0] == "P":
#         strings.insert(cursor, command[1])
#         cursor += 1
#     else:
#         pass

# print("".join(strings))

import sys

left_stack = list(sys.stdin.readline().strip())
right_stack = []

for _ in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().split()

    if command[0] == "L" and left_stack:
        right_stack.append(left_stack.pop())
    elif command[0] == "D" and right_stack:
        left_stack.append(right_stack.pop())
    elif command[0] == "B" and left_stack:
        left_stack.pop()
    elif command[0] == "P":
        left_stack.append(command[1])

print("".join(left_stack + right_stack[::-1]))

