import sys

words = sys.stdin.readline().rstrip() 

while words != '.':
    words = list(words)
    stack = []
    for w in words:
        if w == '(':
            stack.append(w)
        elif w == '[':
            stack.append(w)
        elif w == ')':
            if not stack or stack[-1] != '(':
                stack.append(w)
                break
            else:
                stack.pop()
        elif w == ']':
            if not stack or stack[-1] != '[':
                stack.append(w)
                break
            else:
                stack.pop()
    if stack:
        print('no')
    else:
        print('yes')
    

    words = sys.stdin.readline().rstrip() 
