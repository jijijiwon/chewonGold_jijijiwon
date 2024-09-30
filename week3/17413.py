import sys

S = sys.stdin.readline().strip()

stack = []
result = []
isTag = False  # 현재 태그 내부에 있는지

for i in range(len(S)):
    if S[i] == '>':
        isTag = False
        result.append(S[i])
    elif isTag:  # 태그 내부인 경우
        result.append(S[i])  # stack이 아닌 result에 추가
    elif S[i] == ' ':
        while stack:  # 스택에 있는 문자들을 모두 팝(역순)하여 결과에 추가
            result.append(stack.pop())
        result.append(S[i])
    elif S[i] == '<':
        isTag = True
        while stack:  # 태그 시작 전에 쌓인 문자들을 모두 팝(역순)하여 결과에 추가
            result.append(stack.pop())
        result.append(S[i])
    else:
        stack.append(S[i])

while stack:
    result.append(stack.pop())

print(''.join(result))
