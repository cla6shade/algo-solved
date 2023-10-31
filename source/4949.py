res = []
while True:
    line = input()
    if line == '.':
        break
    stack = []
    for s in line:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if len(stack) == 0 or stack[len(stack) - 1] != '(':
                stack.append('')
                break
            stack.pop()
        elif s == ']':
            if len(stack) == 0 or stack[len(stack) - 1] != '[':
                stack.append('')
                break
            stack.pop()
    if len(stack) == 0:
        print('yes')
    else:
        print('no')
