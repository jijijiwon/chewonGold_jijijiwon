input_string = str(input())  # 입력 받기

stack = []
anwser = 0

for i in range(len(input_string)):
    if input_string[i] == '(':  # '('일 때는 스택에 넣기
        stack.append('(')

    elif input_string[i] == ')':
        if input_string[i - 1] == '(':  # 직전 문자가 '('라면 레이저
            stack.pop()  # 레이저이므로 '(' 제거
            anwser += len(stack)  # 레이저가 자른 막대기 수는 현재 스택에 남은 '('의 수

        else:  # ')'로 막대기 끝난 경우
            stack.pop()  # 막대기 끝났으므로 '(' 제거
            anwser += 1  # 막대기 끝에 한 조각 추가

print(anwser)
